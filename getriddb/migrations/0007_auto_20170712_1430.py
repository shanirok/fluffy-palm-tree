# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('getriddb', '0006_auto_20170712_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='type',
            new_name='itemtype',
        ),
        migrations.AddField(
            model_name='size',
            name='itemtype',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='getriddb.Type'),
            preserve_default=False,
        ),
    ]