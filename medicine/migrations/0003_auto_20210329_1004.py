# Generated by Django 3.1.7 on 2021-03-29 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_thuoc_stt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thuoc',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
