# Generated by Django 5.0.7 on 2024-08-14 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0019_alter_crowddata_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crowddata',
            name='location',
            field=models.CharField(choices=[('S44', 'TOMIKEN'), ('COMMUNICATIONCAT3', 'プログラム名'), ('GEOROGYLABOLATORY', '地球の正体')], max_length=20),
        ),
    ]
