# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 21:02
from __future__ import unicode_literals

from django.db import migrations
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=django_bleach.models.BleachField(),
        ),
    ]
