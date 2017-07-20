# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getriddb', '0022_auto_20170720_0129'),
    ]

    operations = [
         migrations.AddField(
            model_name='inventoryitem',
            name='brand',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='quality',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='size',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='color',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
         migrations.AddField(
            model_name='inventoryitem',
            name='firstassessment',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
         migrations.AddField(
            model_name='inventoryitem',
            name='donationvalue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='location',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='condition',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='defectdetails',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='cut',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
         migrations.AddField(
            model_name='inventoryitem',
            name='style',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='fabric',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='usecase',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='postprice',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='origprice',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='title',
            field=models.CharField(blank=True, default='', help_text='(updated on save)', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='description',
            field=models.CharField(blank=True, default='', help_text='(updated on save)', max_length=200),
        ),
         migrations.AddField(
            model_name='inventoryitem',
            name='up4saledate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='ebay',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='poshmark',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='tradesy',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='vinted',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='craigslist',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='offerup',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='letgo',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='offline',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='solddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='finalsellingprice',
            field=models.FloatField(blank=True, null=True),
        ),        
        migrations.AddField(
            model_name='inventoryitem',
            name='MKTplacefee',
            field=models.FloatField(blank=True, null=True),
        ),
         migrations.AddField(
            model_name='inventoryitem',
            name='shippingcosts',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='itemprofit',
            field=models.FloatField(default=0, help_text='(updated on save)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='customerpayout',
            field=models.FloatField(default=0, help_text='(updated on save)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='status',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='statuschangedate',
            field=models.DateField(blank=True, null=True),
        ),        
    ]
