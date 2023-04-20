# Generated by Django 4.1.7 on 2023-04-05 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_rename_balance_useraccountnumber_accountbalance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='recipient_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_transactions', to='App.useraccountnumber'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sender_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_transactions', to='App.useraccountnumber'),
        ),
    ]
