# Generated by Django 2.1.7 on 2019-03-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20190323_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinfo',
            name='course_code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='courseinfo',
            name='dept',
            field=models.CharField(default='', max_length=20),
        ),
    ]
