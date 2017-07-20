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
    pickupprice = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.id)

    class Meta:
        db_table = 'pickup'
        
class Inventoryitem(models.Model):
    id = models.AutoField(primary_key=True)
    item_indate = models.DateField(blank=True, null=True)
    item_pickup = models.ForeignKey('Pickup', related_name='Inventoryitems')
    item_category = models.CharField(max_length=200, blank=True, default='')
    item_segment = models.CharField(max_length=200, blank=True, null=True, default='')
    item_type = models.CharField(max_length=200, blank=True, null=True, default='')
    item_brand = models.CharField(max_length=200, blank=True, null=True, default='')
    item_quality = models.CharField(max_length=200, blank=True, null=True, default='')
    item_size = models.CharField(max_length=200,  blank=True, null=True, default='')
    item_color = models.CharField(max_length=200, blank=True, null=True, default='')
    item_firstassessment = models.CharField(max_length=200, blank=True, null=True, default='')
    item_donationvalue = models.FloatField(blank=True, null=True)
    item_condition = models.CharField(max_length=200, blank=True, null=True, default='')
    item_defectdetails = models.CharField(max_length=200, blank=True, null=True, default='')
    item_cut = models.CharField(max_length=200, blank=True, null=True, default='')
    item_style = models.CharField(max_length=200, blank=True, null=True, default='')
    item_fabric = models.CharField(max_length=200, blank=True, null=True, default='')
    item_usecase = models.CharField(max_length=200, blank=True, null=True, default='')
    item_postprice = models.FloatField(blank=True, null=True)
    item_origprice = models.FloatField(blank=True, null=True)
    item_status = models.CharField(max_length=200, blank=True, default='')
    item_statuschangedate = models.DateField(blank=True, null=True)
    item_location = models.CharField(max_length=200, blank=True, null=True, default='')
    item_up4saledate = models.DateField(blank=True, null=True)
    ebay = models.CharField(max_length=200, blank=True, null=True, default='')
    poshmark = models.CharField(max_length=200, blank=True, null=True, default='')
    vinted = models.CharField(max_length=200, blank=True, null=True, default='')
    tradesy = models.CharField(max_length=200, blank=True, null=True, default='')
    craigslist = models.CharField(max_length=200, blank=True, null=True, default='')
    letgo = models.CharField(max_length=200, blank=True, null=True, default='')
    offerup = models.CharField(max_length=200, blank=True, null=True, default='')
    offline = models.CharField(max_length=200, blank=True, null=True, default='')
    item_solddate = models.DateField(blank=True, null=True)
    item_finalsellingprice = models.FloatField(blank=True, null=True)
    MKTplacefee = models.FloatField(blank=True, null=True)
    shippingcosts = models.FloatField(blank=True, null=True)
    
    
    title = models.CharField(max_length=200, blank=True, null=True, default='', help_text="(updated on save)")
    description = models.TextField(max_length=255, blank=True, null=True, default='', help_text="(updated on save)")
    item_profit = models.FloatField(blank=True, null=True, help_text="(updated on save)")
    customerpayout = models.FloatField(blank=True, null=True, help_text="(updated on save)")
    
    #def __init__(self, *args, **kwargs):
        #super(Inventoryitem, self).__init__(*args, **kwargs)
        #self.old_status = self.status

    #def save(self, *args, **kwargs):
     #   if self.old_status != self.status:
     #       self.statuschangedate = datetime.now()
     #   super(Inventoryitem, self).save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        self.title = self.brand + self.color + self.size
        self.description = self.brand + self.color + self.size
        self.itemprofit = float(self.finalsellingprice) - float(self.MKTplacefee) - float(self.shippingcosts)
        self.customerpayout = float(self.itemProfit/2)
        
        super(Product, self).save(*args, **kwargs) 
    
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
    size = models.CharField(max_length=200, blank=False)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.size)
    
class Color(models.Model):
    color = models.CharField(max_length=200, blank=False)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.color)

class Cut(models.Model):
    category =  models.ForeignKey('Category')
    segment =  models.ForeignKey('Segment')
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

    
    
