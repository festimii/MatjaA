import logging
import uuid
import pandas as pd
from datetime import date
from typing import Tuple
from django.core.files.uploadedfile import UploadedFile
from django.db import models, transaction, IntegrityError
from cubaapp.models import ExcelRecord
from typing import Dict, Any
logger = logging.getLogger(__name__)

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


def import_excel_from_file(file_obj: UploadedFile, user, batch_id=None) -> Dict[str, Any]:
    batch_id = batch_id or uuid.uuid4()
    logger.debug("🔄 Starting Excel import")

    file_obj.seek(0)
    df = pd.read_excel(file_obj)
    df.columns = [c.strip() for c in df.columns]

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

    for col in ("prej", "deri"):
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")\
                         .apply(lambda ts: ts.date() if pd.notnull(ts) else None)

    for col in df.columns:
        if col.startswith("vfs_") or col in ("nr", "total_planifikimi_pako"):
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    key_cols = ["sifra_e_artikullit", "prej", "deri"]
    df_valid = df.dropna(subset=key_cols)
    df_skip = df[df[key_cols].isna().any(axis=1)]

    if not df_skip.empty:
        logger.warning("Skipping rows with missing sifra/prej/deri: %s", df_skip.index.tolist())

    duplicate_rows = df_valid.duplicated(subset=key_cols, keep=False)
    if duplicate_rows.any():
        dup_df = df_valid[duplicate_rows]
        dup_keys = dup_df[key_cols].drop_duplicates()
        dup_str = "; ".join(f"{row.sifra_e_artikullit}, {row.prej}, {row.deri}" for _, row in dup_keys.iterrows())
        raise ValueError("Duplicate (sifra, prej, deri) combinations in file: " + dup_str)

    rejected_keys = []
    insertable_rows = []

    for _, row in df_valid.iterrows():
        sifra = str(int(row["sifra_e_artikullit"])).zfill(6)
        prej = row["prej"]
        deri = row["deri"]

        # Overlap logic: (prej_existing <= deri_new) and (deri_existing >= prej_new)
        conflict_exists = ExcelRecord.objects.filter(
            sifra_e_artikullit=sifra,
            user=user,
            prej__lte=deri,
            deri__gte=prej
        ).exists()

        if conflict_exists:
            rejected_keys.append((sifra, prej, deri))
            continue

        insertable_rows.append((row, sifra))

    if rejected_keys:
        reject_str = "; ".join(f"{s} from {p} to {d}" for s, p, d in rejected_keys)
        logger.warning("❌ Rejected due to overlapping intervals: %s", reject_str)

    count = 0
    for row, sifra in insertable_rows:
        data = row.to_dict()
        nr = data.pop("nr")
        data["sifra_e_artikullit"] = sifra
        data["user"] = user
        data["batch_id"] = batch_id

        for field_name, val in data.items():
            if isinstance(val, str):
                fld = ExcelRecord._meta.get_field(field_name)
                maxlen = getattr(fld, "max_length", None)
                if maxlen and len(val) > maxlen:
                    logger.error(
                        "Row %s: field `%s` is %d chars (max=%d)",
                        nr, field_name, len(val), maxlen
                    )
                    data[field_name] = val[:maxlen]

        try:
            with transaction.atomic():
                ExcelRecord.objects.create(nr=nr, **data)
        except IntegrityError as e:
            key = f"{sifra} on {data.get('prej')}"
            logger.error("❌ DB unique constraint violation: %s", key)
            raise ValueError(f"Duplikat në databazë: sifra {sifra} me datën {data.get('prej')} ekziston.")
        except Exception:
            logger.exception("⚠️ Failed to insert row %s: %r", nr, data)
            raise
        else:
            count += 1

    logger.info("✅ Imported %d rows; Skipped %d nulls; Rejected %d overlaps.",
                count, len(df_skip), len(rejected_keys))
    return {
        "imported": count,
        "batch_id": batch_id,
        "skipped": df_skip.index.tolist(),
        "rejected": rejected_keys,  # List of (sifra, prej, deri)
    }
