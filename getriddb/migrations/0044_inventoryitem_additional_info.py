# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getriddb', '0043_auto_20170727_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='additional_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
