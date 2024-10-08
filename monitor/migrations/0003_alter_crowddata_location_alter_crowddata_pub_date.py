# Generated by Django 5.0.7 on 2024-08-07 13:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_alter_crowddata_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crowddata',
            name='location',
            field=models.CharField(choices=[('CM3', 'プログラム名'), ('GML', '地球の正体'), ('S44', 'TOMIKEN')], max_length=20),
        ),
        migrations.AlterField(
            model_name='crowddata',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='pub_date'),
        ),
    ]
