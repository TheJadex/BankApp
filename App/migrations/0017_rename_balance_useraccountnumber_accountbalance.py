# Generated by Django 4.1.7 on 2023-04-05 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0016_useraccountnumber_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccountnumber',
            old_name='balance',
            new_name='accountBalance',
        ),
    ]