# Generated by Django 3.2.5 on 2021-08-16 13:27

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='API_Key',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='API_Secret',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Broker',
            field=models.CharField(blank=True, choices=[('Alice Blue', 'Alice Blue'), ('Angel Broking', 'Angel Broking'), ('Fyers', 'Fyers'), ('Upstox', 'Upstox'), ('Zerodha', 'Zerodha')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Password',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Pin_2FA',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='SubWebHook',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='UserId',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='account_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='PhoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
