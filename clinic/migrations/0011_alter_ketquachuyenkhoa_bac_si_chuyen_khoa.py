# Generated by Django 3.2 on 2021-04-17 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0010_mauphieu_codename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ketquachuyenkhoa',
            name='bac_si_chuyen_khoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ket_qua_bac_si_chuyen_khoa', to=settings.AUTH_USER_MODEL),
        ),
    ]
