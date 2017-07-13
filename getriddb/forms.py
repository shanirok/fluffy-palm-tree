from django import forms
from dal import autocomplete
import datetime

from .models import Inventoryitem, Pickup, Customer, Segment, Type, Brand, Size, Color, Cut, Fabric, Usecase

class InventoryitemForm(forms.ModelForm):
    class Meta:
        model = Inventoryitem
        fields = ('__all__')

    indate = forms.DateField(label='Date entered DB', initial=datetime.date.today, disabled=True)

   # pickup = forms.ModelChoiceField(
   #     queryset=Pickup.objects.all(),
   #     widget=autocomplete.ModelSelect2(url='pickup-autocomplete')
   # )

    category  = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='category-autocomplete'))

    segment = forms.ModelChoiceField(
        queryset=Segment.objects.all(),
        widget=autocomplete.ModelSelect2('segment-autocomplete', forward=['category']),
    )
    
    itemtype = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        widget=autocomplete.ModelSelect2('type-autocomplete', forward=['category', 'segment'])
    )
   
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=autocomplete.ModelSelect2(url='brand-autocomplete')
    )
    
    size = forms.ModelChoiceField(
        queryset=Size.objects.all(),
        widget=autocomplete.ModelSelect2('size-autocomplete', forward=['category', 'segment', 'itemtype'])
    )

    color = forms.ModelChoiceField(
        queryset= Color.objects.all(),
        widget=autocomplete.ModelSelect2('color-autocomplete')
    )

    firstassessment = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='firstassessment-autocomplete'))

    donationvalue = forms.DecimalField (min_value=1, decimal_places=2)

    condition = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='condition-autocomplete'))
    
    cut = forms.ModelMultipleChoiceField(
        queryset= Cut.objects.filter(itemtype=(Type.objects.get(itemtype='Dress').id)),
        widget=forms.CheckboxSelectMultiple
    )
    


    fabric = forms.ModelChoiceField(
        queryset=Fabric.objects.all(),
        widget=autocomplete.ModelSelect2('fabric-autocomplete')
    )

    usecase = forms.ModelChoiceField(
        queryset=Usecase.objects.all(),
        widget=autocomplete.ModelSelect2('usecase-autocomplete')
    )

    postprice = forms.DecimalField (min_value=1, decimal_places=2) 
    origprice = forms.DecimalField (min_value=1, decimal_places=2) 

    status = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='status-autocomplete'))
    
    statuschangedate = forms.DateField(label='Status Changed', initial=datetime.date.today)
    location =  forms.CharField


    #    image = forms.FileField(required=False, widget=forms.FileInput)
# widget=autocomplete.ModelSelect2Multiple(url='cut-autocomplete')
def clean_name(self):
        # do something that validates your data
        return self.cleaned_data["name"]
