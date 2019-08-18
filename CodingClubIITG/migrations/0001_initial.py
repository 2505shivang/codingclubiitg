# Generated by Django 2.2.4 on 2019-08-16 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('status', models.BooleanField(default=True)),
                ('outline', models.CharField(max_length=500)),
                ('details', models.CharField(max_length=30000)),
                ('prereq', models.CharField(max_length=1000)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
