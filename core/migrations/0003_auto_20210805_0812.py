# Generated by Django 3.2.5 on 2021-08-05 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='Validity',
        ),
        migrations.AddField(
            model_name='transaction',
            name='ValidityDay',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='ValidityIOC',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
