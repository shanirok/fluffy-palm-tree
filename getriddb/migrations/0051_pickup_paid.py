# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-29 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getriddb', '0050_auto_20170829_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickup',
            name='paid',
            field=models.BooleanField(default=True),
        ),
    ]
