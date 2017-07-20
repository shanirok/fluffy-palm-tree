# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getriddb', '0026_auto_20170720_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='description',
            field=models.TextField(blank=True, default='', help_text='(updated on save)', null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='title',
            field=models.CharField(blank=True, default='', help_text='(updated on save)', max_length=200, null=True),
        ),
    ]