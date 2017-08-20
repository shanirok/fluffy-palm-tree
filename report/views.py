from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Q
#from django.utils import simplejson
#from django.template import loader

from getriddb.models import Color, Inventoryitem, Customer, Pickup

# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_customers=Customer.objects.filter(last_pickup_date__isnull=False).count()
    num_pickups=Pickup.objects.all().count()
    num_items=Inventoryitem.objects.all().count()
  
    num_items_sold=Inventoryitem.objects.filter(item_status__contains='Shipped').count()
    num_items_donated=Inventoryitem.objects.filter(item_status__contains='Donated').count()

    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'report/index.html',
        context={'num_customers':num_customers,'num_pickups':num_pickups, 'num_items':num_items, 'num_items_sold':num_items_sold,'num_items_donated':num_items_donated},
    )


class CustomerListView(generic.ListView):
    model = Customer
    paginate_by = 100
    template_name = 'report/customer_list.html' 
    def get_queryset(self):
         return Customer.objects.filter(last_pickup_date__isnull=False).order_by('-last_pickup_date')

class PickupListView(generic.ListView):
    model = Pickup
    paginate_by = 100
    template_name = 'report/pickup_list.html' 
    def get_queryset(self):
         return Pickup.objects.all().order_by('pickup.id')

class ItemListView(generic.ListView):
    model = Inventoryitem
    context_object_name = 'item_list'
    paginate_by = 100
    template_name = 'report/item_list.html' 
    def get_queryset(self):
         return Inventoryitem.objects.all().order_by('inventoryitem.id')

def CustomerPickupList(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    pickup_list = Pickup.objects.filter(customer=customer_id).order_by('pickup.pickupdate')
    number_donated = 0 
#    value_donated = 0
    number_sold = 0
    number_listed = 0
 #   total_payout = 0
    for pickup in pickup_list:
     number_donated += Inventoryitem.objects.filter(item_pickup=pickup.id).filter(Q(item_status__contains='Donated') | Q(item_status__contains='Ready4donation')).count();
  #   value_donated = Inventoryitem.objects.filter(item_pickup=pickup.id).aggregate(sum('item_donationvalue'))
     number_sold += Inventoryitem.objects.filter(item_pickup=pickup.id).filter(item_status__contains='Shipped').count();
     number_listed += Inventoryitem.objects.filter(item_pickup=pickup.id).filter(item_status__contains='Up4sale').count();
     #Inventoryitem.objects.filter(item_pickup=pickup.id).aggregate(payout=sum('customerpayout'))
 #    total = total_payout['payout']
  #  return render(request, 'report/customer_pickup_list.html', {'customer':customer, 'pickup_list':pickup_list, 'number_donated':number_donated, 'value_donated':value_donated, 'number_sold':number_sold, 'number_listed':number_listed, 'total_payout':total_payout})
    return render(request, 'report/customer_pickup_list.html', {'customer':customer, 'pickup_list':pickup_list, 'number_donated':number_donated, 'number_sold':number_sold, 'number_listed':number_listed})

def PickupItemList(request, customer_id, pickup_id):
    item_list = Inventoryitem.objects.filter(item_pickup=pickup_id).order_by('inventoryitem.id')
    return render(request, 'report/pickup_item_list.html', {'item_list':item_list})

# def getdetails(request):
#     #country_name = request.POST['country_name']
#     customer_name = request.GET['cus']
#     print ("ajax customer_name", customer_name)

#     result_set = []
#     all_pickups = []
#     answer = str(customer_name[1:-1])
#     selected_customer = Customer.objects.get(customername=answer)
#     print ("selected customer name", selected_customer)
#     all_pickups = Pickups.filter(customer=selected_customer)
#     for pickup in all_pickups:
#         print ("pickup date", pickup.pickupdate)
#         result_set.append({'date': pickup.pickupdate})
#     return HttpResponse(simplejson.dumps(result_set), mimetype='application/json',     content_type='application/json')



#def pickup_list(request, customerid):
#    pickups = Pickup.objects.filter(customer_is=customerid).order_by('pickupdate')
#    return render(request, 'report/customer_list.html', {'pickups':pickups})

# def pickup_list(request):
#     selected_customer = request.POST['customer']
#     customerid=selected_customer.id
#     pickups = Pickup.objects.filter(customer=customerid).order_by('pickupdate')
#     return render(request, 'report/pickup_list.html', {'pickups':pickups})


# class IndexView(generic.ListView):
#     template_name = 'report/index.html'
#     context_object_name = 'customers_summary'

#     def get_queryset(self):
#         return Customer.objects.order_by('id')

# def detail(request, customer_id):
#     customer = Customer.objects.get(id=customer_id)
#     pickups = get_list_or_404(Pickup, customer_id=customer_id)

#     item_list = Inventoryitem.objects.filter(item_pickup=3)

#     return render(request, 'report/detail.html', {'customer':customer, 'item_list': item_list, 'pickup_list':pickups})



# class ResultsView(generic.DetailView):
#     model = Inventoryitem
#     context_object_name = 'item'
#     template_name = 'report/results.html'
    
    
# def vote(request, item_id):
#     p = get_object_or_404(Inventoryitem, pk=item_id)
#     try:
#         selected_choice = p.colors.get(pk=request.POST['color'])
#     except (KeyError, Color.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'report/detail.html', {
#             'item': p,
#             'error_message': "You didn't select a color.",
#         })
#     else:
#      #   selected_choice.votes += 1
#      #   selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('report:results', args=(p.id,)))
