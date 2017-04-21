# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 15:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('UPS', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse', models.IntegerField()),
                ('tracking_num', models.CharField(default='', max_length=50)),
                ('ready', models.BooleanField(default=False)),
                ('arrive', models.BooleanField(default=False)),
                ('load', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='amazon_web.product'),
        ),
    ]