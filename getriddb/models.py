# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from enum import Enum

#class pusize(Enum):
#    Small    =  0
#    Medium   =  1
#    Large    =  2 

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    customername = models.CharField(max_length=200, blank=True, default='')
    customeremail = models.CharField(max_length=200, blank=True, default='')
    customerphone = models.CharField(max_length=200, blank=True, default='')
    customeraddress = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):              # __unicode__ on Python 2
        return str(self.id)

    class Meta:
        db_table = 'customer'

class Pickup(models.Model):
    id = models.AutoField(primary_key=True)
    pickupdate = models.DateField(blank=True, null=True)
    pickupsize = models.CharField(max_length=200, blank=True, default='')
    pickupprice = models.IntegerField(blank=True, null=True)
    customer = models.ForeignKey(Customer)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.id)

    class Meta:
        db_table = 'pickup'
        
class Inventoryitem(models.Model):
    id = models.AutoField(primary_key=True)
    indate = models.DateField(blank=True, null=True)
    pickup = models.ForeignKey('Pickup', related_name='Inventoryitems')
    category = models.CharField(max_length=200, blank=True, default='')
    segment = models.CharField(max_length=200, blank=True, default='')
    itemtype = models.CharField(max_length=200, blank=True, default='')
    brand = models.CharField(max_length=200, blank=True, default='')
    size = models.CharField(max_length=200,  blank=True, default='')
    color = models.CharField(max_length=200, blank=True, default='')
    firstassessment = models.CharField(max_length=200, blank=True, default='')
    donationvalue = models.FloatField(blank=True, null=True)
    condition = models.CharField(max_length=200, blank=True, default='')
    cut = models.CharField(max_length=200, blank=True, default='')
    style = models.CharField(max_length=200, blank=True, default='')
    fabric = models.CharField(max_length=200, blank=True, default='')
    usecase = models.CharField(max_length=200, blank=True, default='')
    postprice = models.FloatField(blank=True, null=True)
    origprice = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, default='')
    statuschangedate = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):              # __unicode__ on Python 2
        return str(self.id)

    class Meta:
        db_table = 'inventoryitem'

class Category(models.Model):
    category = models.CharField(max_length=200, blank=False)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.category)
    
class Segment(models.Model):
    category =  models.ForeignKey('Category')
    segment = models.CharField(max_length=200, blank=False)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.segment)

class Type(models.Model):
    category =  models.ForeignKey('Category')
    segment =  models.ForeignKey('Segment')
    itemtype = models.CharField(max_length=200, blank=False)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.itemtype)

class Brand(models.Model):
    brand = models.CharField(max_length=200, blank=False)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.brand)
    
class Size(models.Model):
    category =  models.ForeignKey('Category')
    segment =  models.ForeignKey('Segment')
    itemtype =  models.ForeignKey('Type')
    size = models.CharField(max_length=200, blank=False)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.size)
    
class Color(models.Model):
    color = models.CharField(max_length=200, blank=False)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.color)

class Cut(models.Model):
    category =  models.ForeignKey('Category')
    itemtype =  models.ForeignKey('Type')
    cut = models.CharField(max_length=200, blank=False)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.cut)

class Fabric(models.Model):
    fabric = models.CharField(max_length=200, blank=False)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.fabric)

class Usecase(models.Model):
    usecase = models.CharField(max_length=200, blank=False)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.usecase)

    
    
