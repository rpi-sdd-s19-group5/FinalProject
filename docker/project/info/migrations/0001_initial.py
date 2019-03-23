# Generated by Django 2.1.7 on 2019-03-17 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prerequisites', models.CharField(max_length=50)),
                ('offered', models.CharField(max_length=20)),
                ('cross_listed', models.CharField(max_length=50)),
                ('credit_hours', models.IntegerField()),
            ],
        ),
    ]