# Generated by Django 4.1.7 on 2023-05-29 14:09

import App.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_deposit_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='account_number',
            field=App.models.EncryptedField(max_length=255, unique=True),
        ),
    ]