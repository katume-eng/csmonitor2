# Generated by Django 5.0.7 on 2024-08-14 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0018_alter_crowddata_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crowddata',
            name='location',
            field=models.CharField(choices=[('S44', 'TOMIKEN'), ('GEOROGYLABOLATORY', '地球の正体'), ('COMMUNICATIONCAT3', 'プログラム名')], max_length=20),
        ),
    ]
