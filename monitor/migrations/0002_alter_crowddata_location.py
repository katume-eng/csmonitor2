# Generated by Django 5.0.6 on 2024-08-02 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crowddata',
            name='location',
            field=models.CharField(choices=[('GML', '地球の正体'), ('S44', 'TOMIKEN'), ('CM3', 'プログラム名')], max_length=20),
        ),
    ]
