# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('href', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
