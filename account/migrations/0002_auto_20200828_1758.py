# Generated by Django 3.1 on 2020-08-28 12:28

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to=account.models.upload_location),
        ),
    ]
