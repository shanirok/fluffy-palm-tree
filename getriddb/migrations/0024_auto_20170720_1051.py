# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getriddb', '0023_auto_20170720_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='craigslist',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='customerpayout',
            field=models.FloatField(blank=True, help_text='(updated on save)', null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='description',
            field=models.TextField(blank=True, default='', help_text='(updated on save)'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='ebay',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='fabric',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='itemprofit',
            field=models.FloatField(blank=True, help_text='(updated on save)', null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='letgo',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='location',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='offerup',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='offline',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='poshmark',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='quality',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='style',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='tradesy',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='usecase',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='vinted',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
