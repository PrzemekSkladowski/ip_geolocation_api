# Generated by Django 5.2.1 on 2025-05-18 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip_geolocation_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geolocationinfo',
            name='address_data',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]
