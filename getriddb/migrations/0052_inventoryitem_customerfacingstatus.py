# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getriddb', '0051_pickup_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='customerfacingstatus',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
