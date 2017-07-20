from django import forms
from dal import autocomplete
import datetime

from .models import Inventoryitem, Pickup, Customer, Segment, Type, Brand, Size, Color, Cut, Fabric, Usecase

class InventoryitemForm(forms.ModelForm):    
        
    class Meta:
        model = Inventoryitem
        fields = ('__all__')

    item_indate = forms.DateField(label='Date entered DB', initial=datetime.date.today, disabled=True)

    item_pickup = forms.ModelChoiceField(
        label='Pickup #',
        queryset=Pickup.objects.all(),
        widget=autocomplete.ModelSelect2(url='pickup-autocomplete')
    )

    item_category  = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='category-autocomplete'))

    item_segment = forms.ModelChoiceField(
        queryset=Segment.objects.all(),
        widget=autocomplete.ModelSelect2('segment-autocomplete', forward=['category']),
    )
    
    item_type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        widget=autocomplete.ModelSelect2('type-autocomplete', forward=['category', 'segment']),
    )
   
    item_brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=autocomplete.ModelSelect2(url='brand-autocomplete')
    )
    
    item_size = forms.ModelChoiceField(
        queryset=Size.objects.all(),
        widget=autocomplete.ModelSelect2('size-autocomplete', forward=['category', 'segment'])
    )

    item_color = forms.ModelChoiceField(
        queryset= Color.objects.all(),
        widget=autocomplete.ModelSelect2('color-autocomplete')
    )

    item_firstassessment = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='firstassessment-autocomplete'))

    item_donationvalue = forms.DecimalField (min_value=1, decimal_places=2, required=False)

    item_condition = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='condition-autocomplete'),required=False)

    #  itemtypeid=Type.objects.get(itemtype=itemtype).id
    #cut_choices=Cut.objects.filter(itemtype=itemtypeid)
    # cut_choices = [('', 'None')] + [(cut, cut) for cut in Cut.objects.filter(itemtype=(itemtypeid))]
   # cut = forms.ChoiceField(
   #     cut_choices,
   #     required=False,
   #     widget=autocomplete.ModelSelect2Multiple(),
   # )

     # cut = forms.ModelMultipleChoiceField(
   #     queryset= Cut.objects.all(),
   #     widget=forms.CheckboxSelectMultiple(),
   # )

    item_cut = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Cut.objects.all(),
        widget=autocomplete.ModelSelect2Multiple('cut-autocomplete', forward=['itemtype']),
    )
    
    item_fabric = forms.ModelMultipleChoiceField(
        queryset=Fabric.objects.all(),
        widget=autocomplete.ModelSelect2Multiple('fabric-autocomplete'),
        required=False,
    )

    item_usecase = forms.ModelMultipleChoiceField(
        queryset=Usecase.objects.all(),
        widget=autocomplete.ModelSelect2Multiple('usecase-autocomplete'),
        required=False,
    )

    item_postprice = forms.DecimalField (min_value=1, decimal_places=2, required=False,) 
    item_origprice = forms.DecimalField (min_value=1, decimal_places=2, required=False,) 

   # status =  forms.ChoiceField(choices=[('',None),(1,'Sold')]) 
    item_status = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='status-autocomplete'))
    
    item_statuschangedate = forms.DateField(label='Status Changed', initial=datetime.date.today)
    item_location =  forms.CharField(required=False,)

    ebay = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'))
    poshmark = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'))
    vinted = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'))
    tradesy = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'))
    craigslist = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'))
    letgo = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'))
    offerup = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'))
    offline = forms.ChoiceField(choices=[('',None),(1,'Sold')]) 
    
    def __init__(self, *args, **kwargs):
        super(InventoryitemForm, self).__init__(auto_id=True, *args, **kwargs)
    #    self.old_status = self.status

  #  def save(self, *args, **kwargs):
  #      if self.old_status != self.status:
  #          self.statuschangedate = datetime.now()
  #      super(Model, self).save(*args, **kwargs)
    
   # def clean_name(self):
        # do something that validates your data
   #     cleaned_data = super(InventoryitemForm, self).clean()
        #firstassessment = cleaned_data.get("firstassessment")

        #return self.cleaned_data["name"]
    #if firstassessment == 'Sale':
     #   raise forms.ValidationError("A venue is required for events")




    #    image = forms.FileField(required=False, widget=forms.FileInput)
    # widget=autocomplete.ModelSelect2Multiple(url='cut-autocomplete')
