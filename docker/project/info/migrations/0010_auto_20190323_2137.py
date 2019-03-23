# Generated by Django 2.1.7 on 2019-03-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_profinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profinfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profinfo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='profinfo',
            name='dept',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
