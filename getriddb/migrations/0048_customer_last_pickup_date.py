# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-11 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getriddb', '0047_inventoryitem_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='last_pickup_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
