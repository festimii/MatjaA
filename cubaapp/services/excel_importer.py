import logging
from datetime import date

import pandas as pd
from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import FieldDoesNotExist
from django.db import models, transaction, DataError

from cubaapp.models import ExcelRecord

logger = logging.getLogger(__name__)

# 1) Explicit header → model field mapping for the non-VFS fields
HEADER_MAP = {
    "Nr.":                      "nr",
    "Emri I Aksionit":          "emri_i_aksionit",
    "Prej (D/M/Y):":            "prej",
    "Deri (D/M/Y):":            "deri",
    "Furnitori":                "furnitori",
    "Shifra e Artikullit":      "sifra_e_artikullit",
    "Emertimi I artikullit":    "emertimi_i_artikullit",
    "Pako (Ame)":               "pako_ame",
    "Total Planifikimi (PAKO)": "total_planifikimi_pako",
}

def import_excel_from_file(file_obj: UploadedFile) -> int:
    """
    Reads an uploaded Excel file and upserts rows into ExcelRecord.
    - Normalizes `sifra_e_artikullit` to exactly 6 digits (zero-padded).
    - Pre-logs any string fields that exceed their max_length.
    - Silently truncates strings to fit the DB schema.
    Returns the number of rows successfully processed.
    """
    logger.debug("🔄 Starting Excel import")

    # --- Read into DataFrame ---
    file_obj.seek(0)
    df = pd.read_excel(file_obj)
    df.columns = [c.strip() for c in df.columns]

    # --- Rename headers & filter to model fields ---
    model_fields = {
        f.name
        for f in ExcelRecord._meta.get_fields()
        if isinstance(f, models.Field) and not f.auto_created
    }
    full_map = {}
    for hdr, fld in HEADER_MAP.items():
        if hdr in df.columns and fld in model_fields:
            full_map[hdr] = fld
    for hdr in df.columns:
        if hdr.startswith("VFS"):
            fld = hdr.lower().replace(" ", "_")
            if fld in model_fields:
                full_map[hdr] = fld

    df = df.rename(columns=full_map)[list(full_map.values())]

    # --- Coerce types ---
    for col in ("prej", "deri"):
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")\
                         .apply(lambda ts: ts.date() if pd.notnull(ts) else None)

    for col in df.columns:
        if col.startswith("vfs_") or col in ("nr", "total_planifikimi_pako"):
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    # --- Split valid vs invalid: must have both code & date ---
    key_cols = ["sifra_e_artikullit", "prej"]
    df_valid = df.dropna(subset=key_cols)
    df_skip = df[df[key_cols].isna().any(axis=1)]
    if not df_skip.empty:
        logger.warning(
            "Skipping %d rows missing sifra or prej: %s",
            len(df_skip),
            df_skip.index.tolist()
        )

    # --- Check in-file duplicates ---
    dupes = df_valid["sifra_e_artikullit"][
        df_valid["sifra_e_artikullit"].duplicated(keep=False)
    ]
    if not dupes.empty:
        vals = sorted(set(dupes.tolist()))
        raise ValueError("Duplicate codes in file: " + ", ".join(str(v) for v in vals))

    # --- Check cross-DB conflicts ---
    combos = df_valid[key_cols].drop_duplicates().to_records(index=False)
    conflicts = [
        (s, d) for s, d in combos
        if ExcelRecord.objects.filter(sifra_e_artikullit=s, prej=d).exists()
    ]
    if conflicts:
        msg = "; ".join(f"{s} on {d}" for s, d in conflicts)
        raise ValueError("Conflicting code+date in DB: " + msg)

    # --- Upsert only valid rows ---
    count = 0
    for _, row in df_valid.dropna(subset=["nr"]).iterrows():
        data = row.to_dict()
        nr = data.pop("nr")

        # 1) Normalize `sifra_e_artikullit` to 6 digits
        raw_code = data.get("sifra_e_artikullit")
        if raw_code is not None:
            try:
                code_int = int(raw_code)
                data["sifra_e_artikullit"] = str(code_int).zfill(6)
            except (ValueError, TypeError):
                raise ValueError(f"Invalid sifra_e_artikullit: {raw_code!r} on row {nr}")

        # 2) Preflight: log any field exceeding its max_length
        for field_name, val in data.items():
            if isinstance(val, str):
                fld = ExcelRecord._meta.get_field(field_name)
                maxlen = getattr(fld, "max_length", None)
                if maxlen and len(val) > maxlen:
                    logger.error(
                        "Row %s: field `%s` is %d chars (max=%d)",
                        nr, field_name, len(val), maxlen
                    )
                    # 3) Truncate to fit
                    data[field_name] = val[:maxlen]

        try:
            with transaction.atomic():
                ExcelRecord.objects.update_or_create(nr=nr, defaults=data)
        except DataError:
            logger.exception("Failed to import row %s: %r", nr, data)
            raise
        else:
            count += 1

    logger.debug("Imported %d rows; skipped %d", count, len(df_skip))
    return count
