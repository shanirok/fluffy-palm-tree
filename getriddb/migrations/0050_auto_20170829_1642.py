# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-29 20:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getriddb', '0049_payout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payout',
            old_name='customerpaid',
            new_name='customer',
        ),
    ]
