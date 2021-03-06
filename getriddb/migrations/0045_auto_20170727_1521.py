# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getriddb', '0044_inventoryitem_additional_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='usecases',
            field=models.ManyToManyField(to='getriddb.Usecase'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='additional_info',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
