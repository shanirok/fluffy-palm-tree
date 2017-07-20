# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from dal import autocomplete

from getriddb.models import Inventoryitem, Pickup, Category, Segment, Type, Brand, Size, Color, Cut, Fabric, Usecase
from getriddb.forms import InventoryitemForm

# Create your views here.

class PickupAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return pickup.objects.none()

        qs = Pickup.objects.all()

        if self.q:
            qs = qs.filter(id__istartswith=self.q)

        return qs


class CategoryModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return category.objects.none()

        qs = Category.objects.all()

        if self.q:
            qs = qs.filter(category__istartswith=self.q)
            
        return qs
    def create_object(self, text):
        """Create an object given a text."""
        return self.get_queryset().create(**{self.create_field: text})

    
class SegmentModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return segment.objects.none()

        category = self.forwarded.get('category', None)

        qs = Segment.objects.all()

        if category:
            qs = qs.filter(category=category)
            
        if self.q:
            qs = qs.filter(segment__istartswith=self.q)
            
        return qs

    def create_object(self, text):
        """Create an object given a text."""
        category = self.forwarded.get('category', None)
        return self.get_queryset().create(category_id=category, segment=text)
    

class TypeModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return type.objects.none()

        category = self.forwarded.get('category', None)
        segment = self.forwarded.get('segment', None)
        
        qs = Type.objects.all()

        if category:
            qs = qs.filter(category=category, segment=segment)
            
        if self.q:
            qs = qs.filter(itemtype__istartswith=self.q)
            
        return qs
    
    def create_object(self, text):
        """Create an object given a text."""
        category = self.forwarded.get('category', None)
        segment = self.forwarded.get('segment', None)
        return self.get_queryset().create(category_id=category, segment_id=segment, itemtype=text)

class BrandModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return brand.objects.none()

        qs = Brand.objects.all()

        if self.q:
            qs = qs.filter(brand__istartswith=self.q)
            
        return qs

class SizeModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return size.objects.none()

        category = self.forwarded.get('category', None)
        segment = self.forwarded.get('segment', None)                      
        
        qs = Size.objects.all()

        if category:
            qs = qs.filter(category=category, segment=segment)
            
        if self.q:
            qs = qs.filter(size__istartswith=self.q)
            
        return qs
    
    def create_object(self, text):
        """Create an object given a text."""
        category = self.forwarded.get('category', None)
        segment = self.forwarded.get('segment', None)
        itemtype = self.forwarded.get('itemtype', None)
        return self.get_queryset().create(category_id=category, segment_id=segment, itemtype_id=itemtype, size=text)

    
  
class ColorModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return color.objects.none()

        qs = Color.objects.all()

        if self.q:
            qs = qs.filter(color__istartswith=self.q)
            
        return qs

class FirstassessmentAutocompleteFromList(autocomplete.Select2ListView):
    def get_list(self):
        return ['Sale', 'Donation', 'Recycling']

class ConditionAutocompleteFromList(autocomplete.Select2ListView):
    def get_list(self):
        return ['New in a box', 'New w/o tags', 'New w tags', 'Like new', 'Gently used', 'Used', 'w defect']


class CutModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return cut.objects.none()

        itemtype = self.forwarded.get('itemtype', None) 
        qs = Cut.objects.all()

        if itemtype:
            qs = qs.filter(itemtype=itemtype)
            
        if self.q:
            qs = qs.filter(cut__istartswith=self.q)
            
        return qs

    def create_object(self, text):
        """Create an object given a text."""
        itemtype = self.forwarded.get('itemtype', None)
        return self.get_queryset().create(itemtype_id=itemtype, cut=text)
    
class FabricModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return fabric.objects.none()

        qs = Fabric.objects.all()

        if self.q:
            qs = qs.filter(fabric__istartswith=self.q)
            
        return qs

class UsecaseModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return usecase.objects.none()

        qs = Usecase.objects.all()

        if self.q:
            qs = qs.filter(usecase__istartswith=self.q)
            
        return qs

class StatusAutocompleteFromList(autocomplete.Select2ListView):
    def get_list(self):
        return ['Ready4donation', 'Ready4sale', 'Ready4recycling', 'Donated', 'Up4sale', 'Ready2ship', 'Shipped', 'Recycled', 'Treatment', 'Returned']

class MktplaceAutocompleteFromList(autocomplete.Select2ListView):
    def get_list(self):
        return ['Up', 'Down', 'Sold', 'Returned']
