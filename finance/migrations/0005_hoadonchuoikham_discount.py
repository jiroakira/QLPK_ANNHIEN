# Generated by Django 3.2 on 2021-04-16 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_auto_20210406_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoadonchuoikham',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
