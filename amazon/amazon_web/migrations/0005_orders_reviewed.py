# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon_web', '0004_auto_20170428_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
