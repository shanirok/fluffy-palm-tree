from django.conf.urls import include, url

#from dal import autocomplete

from . import views
from .models import Pickup, Inventoryitem, Category, Segment, Type, Brand, Size, Color, Cut, Fabric, Usecase

urlpatterns = [
#### PICKUP ####    
    url(r'^pickup-autocomplete/$', views.PickupAutocomplete.as_view(), name='pickup-autocomplete',),

#### CATEGORY ####    
    url(r'^category-autocomplete/$',
        views.CategoryModelAutocomplete.as_view(
            model = Category,
            create_field='category',
        ),
        name='category-autocomplete',),
#### SEGMENT ####
    url(r'^segment-autocomplete/$',
        views.SegmentModelAutocomplete.as_view(
            model = Segment,
            create_field='segment',
        ),
        name='segment-autocomplete',        
    ),
#### TYPE ####    
    url(r'^type-autocomplete/$',
        views.TypeModelAutocomplete.as_view(
            model=Type,
            create_field='itemtype',
        ),
        name='type-autocomplete',
    ),
#### BRAND ####        
    url(r'^brand-autocomplete/$',
        views.BrandModelAutocomplete.as_view(
            model=Brand,
            create_field='brand',
        ),
        name='brand-autocomplete',
    ),
#### SIZE ####    
    url(r'^size-autocomplete/$',
        views.SizeModelAutocomplete.as_view(
            model=Size,
            create_field='size',
        ),
        name='size-autocomplete',
    ),
#### COLOR ####   
    url(r'^color-autocomplete/$',
        views.ColorModelAutocomplete.as_view(
            model=Color,
            create_field='color',
        ),
        name='color-autocomplete',
    ),
#### FIRSTASSESSMENT ####   
    url(r'^firstassessment-autocomplete/$',
        views.FirstassessmentAutocompleteFromList.as_view(),
        name='firstassessment-autocomplete',
    ),
#### CONDITION ####   
    url(r'^condition-autocomplete/$',
        views.ConditionAutocompleteFromList.as_view(),
        name='condition-autocomplete',
    ),
#### CUT ####   
    url(r'^cut-autocomplete/$',
         views.CutModelAutocomplete.as_view(
             model=Cut,
             create_field='cut',
         ),
        name='cut-autocomplete',
    ),
    
#### FABRIC ####   
    url(r'^fabric-autocomplete/$',
        views.FabricModelAutocomplete.as_view(
            model=Fabric,
            create_field='fabric',
        ),
        name='fabric-autocomplete',
    ),

#### USECASE ####   
    url(r'^usecase-autocomplete/$',
        views.UsecaseModelAutocomplete.as_view(
            model=Usecase,
            create_field='usecase',
        ),
        name='usecase-autocomplete',
    ),

#### STATUS ####   
    url(r'^status-autocomplete/$',
        views.StatusAutocompleteFromList.as_view(),
        name='status-autocomplete',
    ),

#### CUSTOMER STATUS ####   
    url(r'^customerstatus-autocomplete/$',
        views.CustomerStatusAutocompleteFromList.as_view(),
        name='customerstatus-autocomplete',
    ),

#### MKTPLACE ####   
    url(r'^mktplace-autocomplete/$',
        views.MktplaceAutocompleteFromList.as_view(),
        name='mktplace-autocomplete',
    ),
]
