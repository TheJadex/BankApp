# Generated by Django 4.1.7 on 2023-04-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_remove_deposit_user_first_name_deposit_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='user_first_name',
            field=models.CharField(default='first_name', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deposit',
            name='user_last_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deposit',
            name='user_username',
            field=models.CharField(default='192', max_length=30),
            preserve_default=False,
        ),
    ]
