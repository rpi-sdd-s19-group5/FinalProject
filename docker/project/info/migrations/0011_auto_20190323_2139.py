# Generated by Django 2.1.7 on 2019-03-23 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_auto_20190323_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profinfo',
            name='dept',
            field=models.TextField(blank=True, null=True),
        ),
    ]
