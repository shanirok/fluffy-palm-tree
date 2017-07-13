# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    customername = models.CharField(max_length=-1, blank=True, null=True)
    customeremail = models.CharField(max_length=-1, blank=True, null=True)
    customerphone = models.CharField(max_length=-1, blank=True, null=True)
    customeraddress = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Inventory(models.Model):
    indate = models.DateField(blank=True, null=True)
    pickup_id = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=-1, blank=True, null=True)
    segment = models.CharField(max_length=-1, blank=True, null=True)
    itemtype = models.CharField(max_length=-1, blank=True, null=True)
    brand = models.CharField(max_length=-1, blank=True, null=True)
    size = models.CharField(max_length=-1, blank=True, null=True)
    color = models.CharField(max_length=-1, blank=True, null=True)
    firstassessment = models.CharField(max_length=-1, blank=True, null=True)
    donationvalue = models.FloatField(blank=True, null=True)
    condition = models.CharField(max_length=-1, blank=True, null=True)
    cut = models.CharField(max_length=-1, blank=True, null=True)
    style = models.CharField(max_length=-1, blank=True, null=True)
    fabric = models.CharField(max_length=-1, blank=True, null=True)
    usecase = models.CharField(max_length=-1, blank=True, null=True)
    postprice = models.FloatField(blank=True, null=True)
    origprice = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=-1, blank=True, null=True)
    statuschangedate = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'


class Pickup(models.Model):
    pickupdate = models.DateField(blank=True, null=True)
    pickupsize = models.CharField(max_length=-1, blank=True, null=True)
    pickupprice = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pickup'


class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'
