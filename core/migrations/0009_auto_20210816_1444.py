# Generated by Django 3.2.5 on 2021-08-16 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_auto_20210816_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActivateCopyTrade', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Bucket_Creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Bucket',
                'verbose_name_plural': 'Buckets',
            },
        ),
        migrations.CreateModel(
            name='Multiplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multiplier', models.PositiveIntegerField(default=1)),
                ('Bucket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.bucket')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bucket',
            name='Users',
            field=models.ManyToManyField(through='core.Multiplier', to=settings.AUTH_USER_MODEL),
        ),
    ]
