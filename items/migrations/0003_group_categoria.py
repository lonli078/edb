# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.Categories'),
        ),
    ]
