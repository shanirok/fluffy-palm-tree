# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from getriddb.models import Customer, Pickup, Inventoryitem, Category, Segment, Type, Brand, Size, Color, Cut, Fabric, Usecase
from getriddb.forms import InventoryitemForm

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customername', 'customeremail', 'customerphone', 'customeraddress')

class PickupAdmin(admin.ModelAdmin):
    list_display = ('id', 'pickupdate', 'pickupsize', 'pickupprice', 'customer')

    
class InventoryitemAdmin(admin.ModelAdmin):    
    list_display = ('id', 'pickup', 'itemtype', 'brand', 'firstassessment')
    list_filter = ['firstassessment']
    search_fields = ['brand']
    list_per_page = 1000
    form = InventoryitemForm
    fieldsets = (
        (None, {
            'fields': ('indate', 'pickup', 'category', 'segment', 'itemtype', 'brand', 'size', 'color', 'firstassessment', 'donationvalue')
        }),
        ('If item is for sale', {
            'classes': ('collapse',),
            'fields': ('condition', 'cut', 'fabric', 'usecase', 'postprice', 'origprice'),
        }),
        ('Update Status', {
            'fields': ('status', 'statuschangedate', 'location'),
        }),
    )
    
class SegmentAdmin(admin.ModelAdmin):
    list_display = ('category', 'segment')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('category', 'segment', 'itemtype')

class SizeAdmin(admin.ModelAdmin):
    list_display = ('category', 'segment', 'itemtype', 'size')

class CutAdmin(admin.ModelAdmin):
    list_display = ('category', 'itemtype', 'cut')

        
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Pickup, PickupAdmin)
admin.site.register(Inventoryitem, InventoryitemAdmin)
admin.site.register(Category)
admin.site.register(Segment, SegmentAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Brand)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color)
admin.site.register(Cut, CutAdmin)
admin.site.register(Fabric)
admin.site.register(Usecase)

