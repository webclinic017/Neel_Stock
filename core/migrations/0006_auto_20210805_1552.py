# Generated by Django 3.2.5 on 2021-08-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210805_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='Stock',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='Stockexch_seg',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='Stockname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='Stocksymbol',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='Stocktoken',
            field=models.CharField(max_length=200, null=True),
        ),
    ]