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

#    list_display = ('id', 'pickup', 'itemtype', 'brand', 'firstassessment')
 # list_filter = ['firstassessment']
    # search_fields = ['id', 'brand']
class InventoryitemAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("my_styles.css",)
        }
        js = ("getriddb/js/my_code.js",)

    list_display = ('id','item_pickup', 'item_type', 'item_brand', 'item_firstassessment')
        
    list_per_page = 200
    form = InventoryitemForm
        #fields = ('__all__')
    readonly_fields = ('title','description', 'item_profit', 'customerpayout')
    fieldsets = (
         (None, {
             'fields': ('item_indate', 'item_pickup', 'item_category', 'item_segment', 'item_type', 'item_brand', 'item_size', 'item_color', 'item_firstassessment', 'item_donationvalue')
         }),
         ('If item is for sale', {
             'classes': ('forsale',),
             'fields': ('item_condition', 'item_cut', 'item_fabric', 'item_usecase', 'item_postprice', 'item_origprice'),
         }),
         ('Update Status', {
             'fields': ('item_status', 'item_statuschangedate', 'item_location'),
         }),
         ('Up for sale', {
             'classes': ('upforsale',),
             'fields': ('title', 'description', 'item_up4saledate', ('ebay', 'poshmark', 'vinted', 'tradesy', 'craigslist', 'letgo', 'offerup', 'offline'), 'item_solddate', 'item_finalsellingprice', 'MKTplacefee', 'shippingcosts', 'item_profit', 'customerpayout'),
         }),
    )

    
#    def clean(self):
        # Don't allow draft entries to have a pub_date.
#        if self.status == 'draft' and self.pub_date is not None:
#            raise ValidationError(_('Draft entries may not have a publication date.'))
        # Set the pub_date for published items if it hasn't been set already.
#        if self.status == 'ready4sale' and self.statuschangedate is None:
#            self.statuschangedate = datetime.date.today()

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    
class SegmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'segment')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'segment', 'itemtype')

class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'segment', 'size')

class CutAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'segment', 'itemtype', 'cut')

        
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Pickup, PickupAdmin)
admin.site.register(Inventoryitem, InventoryitemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Segment, SegmentAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Brand)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color)
admin.site.register(Cut, CutAdmin)
admin.site.register(Fabric)
admin.site.register(Usecase)

