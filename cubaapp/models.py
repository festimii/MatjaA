import uuid

from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
User = get_user_model()
from cuba import settings
from django.conf import settings


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExcelRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nr = models.PositiveIntegerField("Nr.", null=True, blank=True)
    emri_i_aksionit = models.CharField(
        "Emri I Aksionit",
        max_length=500,       # ↑ was 255
    )
    prej = models.DateField("Prej (D/M/Y)", null=True, blank=True)
    deri = models.DateField("Deri (D/M/Y)", null=True, blank=True)
    furnitori = models.CharField(
        "Furnitori",
        max_length=500,       # ↑ was 255
        null=True,
        blank=True,
    )
    sifra_e_artikullit = models.CharField(
        "Shifra e Artikullit",
        max_length=6,
        validators=[
            RegexValidator(
                regex=r'^\d{1,6}$',
                message="Must be 1 to 6 digits",
                code="invalid_sifra"
            )
        ],
        help_text="Enter up to 6 digits; saved as zero-padded 6-digit code."
    )
    emertimi_i_artikullit = models.CharField(
        "Emertimi I Artikullit",
        max_length=500,       # ↑ was 255
    )
    pako_ame = models.TextField(
        "Pako (Ame)",
        null=True,
        blank=True,
        help_text="Any length of text describing the package",
    )
    total_planifikimi_pako = models.IntegerField(
        "Total Planifikimi (PAKO)",
        null=True,
        blank=True
    )
    batch_id = models.UUIDField(default=uuid.uuid4, db_index=True)

    vfs_1 = models.IntegerField("VFS 1", null=True, blank=True)
    vfs_2 = models.IntegerField("VFS 2", null=True, blank=True)
    vfs_3 = models.IntegerField("VFS 3", null=True, blank=True)
    vfs_4 = models.IntegerField("VFS 4", null=True, blank=True)
    vfs_7 = models.IntegerField("VFS 7", null=True, blank=True)
    vfs_8 = models.IntegerField("VFS 8", null=True, blank=True)
    vfs_9 = models.IntegerField("VFS 9", null=True, blank=True)
    vfs_10 = models.IntegerField("VFS 10", null=True, blank=True)
    vfs_11 = models.IntegerField("VFS 11", null=True, blank=True)
    vfs_12 = models.IntegerField("VFS 12", null=True, blank=True)
    vfs_13 = models.IntegerField("VFS 13", null=True, blank=True)
    vfs_14 = models.IntegerField("VFS 14", null=True, blank=True)
    vfs_15 = models.IntegerField("VFS 15", null=True, blank=True)
    vfs_16 = models.IntegerField("VFS 16", null=True, blank=True)
    vfs_17 = models.IntegerField("VFS 17", null=True, blank=True)
    vfs_18 = models.IntegerField("VFS 18", null=True, blank=True)
    vfs_19 = models.IntegerField("VFS 19", null=True, blank=True)
    vfs_20 = models.IntegerField("VFS 20", null=True, blank=True)
    vfs_21 = models.IntegerField("VFS 21", null=True, blank=True)
    vfs_22 = models.IntegerField("VFS 22", null=True, blank=True)
    vfs_23 = models.IntegerField("VFS 23", null=True, blank=True)
    vfs_24 = models.IntegerField("VFS 24", null=True, blank=True)
    vfs_25 = models.IntegerField("VFS 25", null=True, blank=True)
    vfs_26 = models.IntegerField("VFS 26", null=True, blank=True)
    vfs_27 = models.IntegerField("VFS 27", null=True, blank=True)
    vfs_28 = models.IntegerField("VFS 28", null=True, blank=True)
    vfs_29 = models.IntegerField("VFS 29", null=True, blank=True)
    vfs_30 = models.IntegerField("VFS 30", null=True, blank=True)
    vfs_34 = models.IntegerField("VFS 34", null=True, blank=True)
    vfs_36 = models.IntegerField("VFS 36", null=True, blank=True)
    vfs_37 = models.IntegerField("VFS 37", null=True, blank=True)
    vfs_38 = models.IntegerField("VFS 38", null=True, blank=True)
    vfs_39 = models.IntegerField("VFS 39", null=True, blank=True)
    vfs_40 = models.IntegerField("VFS 40", null=True, blank=True)
    vfs_41 = models.IntegerField("VFS 41", null=True, blank=True)
    vfs_42 = models.IntegerField("VFS 42", null=True, blank=True)
    vfs_43 = models.IntegerField("VFS 43", null=True, blank=True)
    vfs_44 = models.IntegerField("VFS 44", null=True, blank=True)
    vfs_45 = models.IntegerField("VFS 45", null=True, blank=True)
    vfs_46 = models.IntegerField("VFS 46", null=True, blank=True)
    vfs_47 = models.IntegerField("VFS 47", null=True, blank=True)
    vfs_48 = models.IntegerField("VFS 48", null=True, blank=True)
    vfs_49 = models.IntegerField("VFS 49", null=True, blank=True)
    vfs_50 = models.IntegerField("VFS 50", null=True, blank=True)
    vfs_51 = models.IntegerField("VFS 51", null=True, blank=True)
    vfs_52 = models.IntegerField("VFS 52", null=True, blank=True)
    vfs_53 = models.IntegerField("VFS 53", null=True, blank=True)
    vfs_54 = models.IntegerField("VFS 54", null=True, blank=True)
    vfs_55 = models.IntegerField("VFS 55", null=True, blank=True)
    vfs_56 = models.IntegerField("VFS 56", null=True, blank=True)
    vfs_57 = models.IntegerField("VFS 57", null=True, blank=True)
    vfs_58 = models.IntegerField("VFS 58", null=True, blank=True)
    vfs_59 = models.IntegerField("VFS 59", null=True, blank=True)
    vfs_60 = models.IntegerField("VFS 60", null=True, blank=True)
    vfs_61 = models.IntegerField("VFS 61", null=True, blank=True)
    vfs_62 = models.IntegerField("VFS 62", null=True, blank=True)
    vfs_63 = models.IntegerField("VFS 63", null=True, blank=True)
    vfs_64 = models.IntegerField("VFS 64", null=True, blank=True)
    vfs_65 = models.IntegerField("VFS 65", null=True, blank=True)
    vfs_66 = models.IntegerField("VFS 66", null=True, blank=True)
    vfs_67 = models.IntegerField("VFS 67", null=True, blank=True)
    vfs_68 = models.IntegerField("VFS 68", null=True, blank=True)
    vfs_69 = models.IntegerField("VFS 69", null=True, blank=True)
    vfs_70 = models.IntegerField("VFS 70", null=True, blank=True)
    vfs_71 = models.IntegerField("VFS 71", null=True, blank=True)
    vfs_72 = models.IntegerField("VFS 72", null=True, blank=True)
    vfs_73 = models.IntegerField("VFS 73", null=True, blank=True)
    vfs_75 = models.IntegerField("VFS 75", null=True, blank=True)
    vfs_76 = models.IntegerField("VFS 76", null=True, blank=True)
    vfs_77 = models.IntegerField("VFS 77", null=True, blank=True)
    vfs_78 = models.IntegerField("VFS 78", null=True, blank=True)
    vfs_79 = models.IntegerField("VFS 79", null=True, blank=True)
    vfs_80 = models.IntegerField("VFS 80", null=True, blank=True)
    vfs_81 = models.IntegerField("VFS 81", null=True, blank=True)
    vfs_82 = models.IntegerField("VFS 82", null=True, blank=True)
    vfs_83 = models.IntegerField("VFS 83", null=True, blank=True)
    vfs_84 = models.IntegerField("VFS 84", null=True, blank=True)
    vfs_85 = models.IntegerField("VFS 85", null=True, blank=True)
    vfs_86 = models.IntegerField("VFS 86", null=True, blank=True)
    vfs_87 = models.IntegerField("VFS 87", null=True, blank=True)
    vfs_88 = models.IntegerField("VFS 88", null=True, blank=True)
    vfs_89 = models.IntegerField("VFS 89", null=True, blank=True)
    vfs_90 = models.IntegerField("VFS 90", null=True, blank=True)
    vfs_91 = models.IntegerField("VFS 91", null=True, blank=True)
    vfs_92 = models.IntegerField("VFS 92", null=True, blank=True)
    vfs_93 = models.IntegerField("VFS 93", null=True, blank=True)
    vfs_94 = models.IntegerField("VFS 94", null=True, blank=True)
    vfs_95 = models.IntegerField("VFS 95", null=True, blank=True)
    vfs_96 = models.IntegerField("VFS 96", null=True, blank=True)
    vfs_97 = models.IntegerField("VFS 97", null=True, blank=True)
    vfs_98 = models.IntegerField("VFS 98", null=True, blank=True)
    vfs_99 = models.IntegerField("VFS 99", null=True, blank=True)
    vfs_100 = models.IntegerField("VFS 100", null=True, blank=True)
    vfs_101 = models.IntegerField("VFS 101", null=True, blank=True)
    vfs_102 = models.IntegerField("VFS 102", null=True, blank=True)
    vfs_103 = models.IntegerField("VFS 103", null=True, blank=True)
    vfs_104 = models.IntegerField("VFS 104", null=True, blank=True)
    vfs_105 = models.IntegerField("VFS 105", null=True, blank=True)
    vfs_106 = models.IntegerField("VFS 106", null=True, blank=True)
    vfs_107 = models.IntegerField("VFS 107", null=True, blank=True)
    vfs_108 = models.IntegerField("VFS 108", null=True, blank=True)
    vfs_109 = models.IntegerField("VFS 109", null=True, blank=True)
    vfs_110 = models.IntegerField("VFS 110", null=True, blank=True)
    vfs_111 = models.IntegerField("VFS 111", null=True, blank=True)
    vfs_112 = models.IntegerField("VFS 112", null=True, blank=True)
    vfs_113 = models.IntegerField("VFS 113", null=True, blank=True)
    vfs_114 = models.IntegerField("VFS 114", null=True, blank=True)
    vfs_115 = models.IntegerField("VFS 115", null=True, blank=True)
    vfs_116 = models.IntegerField("VFS 116", null=True, blank=True)
    vfs_117 = models.IntegerField("VFS 117", null=True, blank=True)
    vfs_118 = models.IntegerField("VFS 118", null=True, blank=True)
    vfs_119 = models.IntegerField("VFS 119", null=True, blank=True)
    vfs_120 = models.IntegerField("VFS 120", null=True, blank=True)
    vfs_121 = models.IntegerField("VFS 121", null=True, blank=True)
    vfs_122 = models.IntegerField("VFS 122", null=True, blank=True)
    vfs_202 = models.IntegerField("VFS 202", null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["sifra_e_artikullit", "prej"],
                name="unique_sifra_per_date"
            )
        ]
    def __str__(self):
        return f"{self.nr} - {self.emri_i_aksionit}"
        # pad sifra_e_artikullit to 6 digitsa
        if self.sifra_e_artikullit:
            self.sifra_e_artikullit = self.sifra_e_artikullit.zfill(6)
        super().save(*args, **kwargs)

class ExcelUploadLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="user_id",
        help_text="The user who performed the upload",
        related_name="excel_uploads",
    )
    username = models.CharField(
        max_length=150,
        editable=False,
        help_text="Snapshot of the username at upload time",
    )
    file_name = models.CharField(
        max_length=255,
        help_text="Original name of the uploaded file",
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        help_text="When the file was uploaded",
    )
    row_count = models.PositiveIntegerField(
        help_text="How many rows were processed",
    )
    batch_id = models.UUIDField(default=uuid.uuid4, db_index=True)

    class Meta:
        ordering = ["-uploaded_at"]
        verbose_name = "Excel Upload Log"
        verbose_name_plural = "Excel Upload Logs"

    def save(self, *args, **kwargs):
        """
        On first save, populate `username` from the related user.
        If the user ever changes their username later, this stays
        locked to the value at upload time.
        """
        # Only overwrite if this is a new record, or username is blank:
        if not self.pk or not self.username:
            self.username = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.username} → {self.file_name} "
            f"@ {self.uploaded_at:%Y-%m-%d %H:%M} "
            f"({self.row_count} rows)"
        )
