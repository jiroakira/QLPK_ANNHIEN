# Generated by Django 3.1.7 on 2021-03-28 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicine', '0001_initial'),
        ('finance', '0001_initial'),
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoadonthuoc',
            name='don_thuoc',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hoa_don_thuoc', to='medicine.donthuoc'),
        ),
        migrations.AddField(
            model_name='hoadonlamsang',
            name='lich_hen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hoa_don_lam_sang', to='clinic.lichhenkham'),
        ),
        migrations.AddField(
            model_name='hoadonchuoikham',
            name='chuoi_kham',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hoa_don_dich_vu', to='clinic.chuoikham'),
        ),
    ]