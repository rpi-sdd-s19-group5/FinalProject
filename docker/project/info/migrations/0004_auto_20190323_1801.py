# Generated by Django 2.1.7 on 2019-03-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20190323_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='cross_listed',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='prerequisites',
            field=models.TextField(),
        ),
    ]
