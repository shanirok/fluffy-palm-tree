from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
#from django.template import loader

from getriddb.models import Color, Inventoryitem, Customer, Pickup

# Create your views here.

def customer_list(request):
    customers = Customer.objects.filter(last_pickup_date__isnull=False).order_by('last_pickup_date')
    return render(request, 'report/customer_list.html', {'customers':customers})

class IndexView(generic.ListView):
    template_name = 'report/index.html'
    context_object_name = 'customers_summary'

    def get_queryset(self):
        return Customer.objects.order_by('id')

def detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    pickups = get_list_or_404(Pickup, customer_id=customer_id)

    item_list = Inventoryitem.objects.filter(item_pickup=3)

    return render(request, 'report/detail.html', {'customer':customer, 'item_list': item_list, 'pickup_list':pickups})



class ResultsView(generic.DetailView):
    model = Inventoryitem
    context_object_name = 'item'
    template_name = 'report/results.html'
    
    
def vote(request, item_id):
    p = get_object_or_404(Inventoryitem, pk=item_id)
    try:
        selected_choice = p.colors.get(pk=request.POST['color'])
    except (KeyError, Color.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'report/detail.html', {
            'item': p,
            'error_message': "You didn't select a color.",
        })
    else:
     #   selected_choice.votes += 1
     #   selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('report:results', args=(p.id,)))
