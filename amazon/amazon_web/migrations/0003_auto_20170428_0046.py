# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 00:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amazon_web', '0002_auto_20170428_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amazon_web.product'),
        ),
    ]
