# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getriddb', '0025_auto_20170720_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='defectdetails',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
