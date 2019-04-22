# Generated by Django 2.2 on 2019-04-20 00:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_archivedpages'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivedpages',
            name='updated_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='relatedpages',
            name='updated_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
