"""my_eb_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from my_eb_site import settings

from dal import autocomplete
from getriddb import views
from getriddb.models import Pickup, Inventoryitem, Category, Segment, Type, Brand, Size, Color, Cut, Fabric, Usecase

urlpatterns = [
    url(r'^admin/', admin.site.urls),
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
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
