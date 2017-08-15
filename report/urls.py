from django.conf.urls import url

from . import views
from getriddb.models import Inventoryitem, Customer, Pickup


urlpatterns = [
    url(r'^$', views.customer_list, name='customer_list'),
    url(r'^$', views.pickup_list, name='pickup_list'),
    

    # ex: /polls/
    url(r'^index$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<customer_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<item_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<item_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<item_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
