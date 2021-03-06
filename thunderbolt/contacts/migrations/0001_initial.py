# Generated by Django 2.2.2 on 2019-06-08 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('number', models.CharField(max_length=15)),
                ('contact_date', models.DateField(default=datetime.datetime.now)),
                ('message', models.TextField(max_length=3000)),
            ],
        ),
    ]
