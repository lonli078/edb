# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 13:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_group_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='last_update',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 13, 13, 34, 58, 126421, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='last_update',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 13, 13, 35, 6, 295142, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
