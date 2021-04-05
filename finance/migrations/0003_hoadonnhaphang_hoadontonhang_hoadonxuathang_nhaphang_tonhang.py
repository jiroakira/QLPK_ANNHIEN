# Generated by Django 3.1.7 on 2021-04-05 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0011_thuoclog_bao_hiem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0002_auto_20210328_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoaDonNhapHang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_hoa_don', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('thoi_gian_tao', models.DateTimeField(blank=True, editable=False, null=True)),
                ('thoi_gian_cap_nhat', models.DateTimeField(blank=True, null=True)),
                ('nguoi_phu_trach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hóa Đơn Nhập Hàng',
            },
        ),
        migrations.CreateModel(
            name='HoaDonTonHang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_hoa_don', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('thoi_gian_tao', models.DateTimeField(blank=True, editable=False, null=True)),
                ('thoi_gian_cap_nhat', models.DateTimeField(blank=True, null=True)),
                ('nguoi_phu_trach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hóa Đơn Tồn Hàng',
            },
        ),
        migrations.CreateModel(
            name='TonHang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_luong', models.PositiveIntegerField()),
                ('thoi_gian_tao', models.DateTimeField(blank=True, editable=False, null=True)),
                ('thoi_gian_cap_nhat', models.DateTimeField(blank=True, null=True)),
                ('hoa_don', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.hoadontonhang')),
                ('thuoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine.thuoc')),
            ],
            options={
                'verbose_name': 'Tồn Hàng',
            },
        ),
        migrations.CreateModel(
            name='NhapHang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_luong', models.PositiveIntegerField(blank=True, null=True)),
                ('bao_hiem', models.BooleanField(default=False)),
                ('thoi_gian_tao', models.DateTimeField(auto_now_add=True, null=True)),
                ('thoi_gian_cap_nhat', models.DateTimeField(auto_now=True, null=True)),
                ('hoa_don', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.hoadonnhaphang')),
                ('thuoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine.thuoc')),
            ],
            options={
                'verbose_name': 'Nhập Hàng',
            },
        ),
        migrations.CreateModel(
            name='HoaDonXuatHang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_hoa_don', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('thoi_gian_tao', models.DateTimeField(blank=True, editable=False, null=True)),
                ('thoi_gian_cap_nhat', models.DateTimeField(blank=True, null=True)),
                ('nguoi_phu_trach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hóa Đơn Nhập Hàng',
            },
        ),
    ]
