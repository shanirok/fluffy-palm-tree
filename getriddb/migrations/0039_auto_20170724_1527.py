# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('getriddb', '0038_auto_20170720_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='MKTplacefee',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='customerpayout',
            field=models.FloatField(blank=True, default=0, help_text='(updated on save)', null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='item_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getriddb.Category', to_field='category'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='item_finalsellingprice',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='item_profit',
            field=models.FloatField(blank=True, default=0, help_text='(updated on save)', null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='shippingcosts',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]