# Generated by Django 4.1.7 on 2023-06-20 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='account_number',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
