# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getriddb', '0019_auto_20170719_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='description',
            field=models.TextField(blank=True, default='', help_text='(updated on save)', max_length=200),
        ),
    ]
