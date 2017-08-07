from django import forms
from django.forms import ModelChoiceField
from dal import autocomplete
import datetime

from .models import Inventoryitem, Pickup, Customer, Category, Segment, Type, Brand, Size, Color, Cut, Fabric, Usecase

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "#%s" % obj.segment

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

  #  item_category  = autocomplete.Select2ListCreateChoiceField(choice_list=None, widget=autocomplete.ListSelect2(url='category-autocomplete'))
   
    item_category = forms.ModelChoiceField(
        label='Item Category',
        queryset=Category.objects.only('category'),
        to_field_name='category',
        widget=autocomplete.ListSelect2(url='category-autocomplete')
    )

    
    
    item_segment = autocomplete.Select2ListCreateChoiceField(choice_list=Segment.objects.all(), widget=autocomplete.ListSelect2(url='segment-autocomplete', forward=['item_category']),)
        
    item_type = autocomplete.Select2ListCreateChoiceField(choice_list=Type.objects.all(), widget=autocomplete.ListSelect2(url='type-autocomplete', forward=['item_category', 'item_segment']), required=False,)
   
    item_brand = autocomplete.Select2ListCreateChoiceField(choice_list=Brand.objects.all(), widget=autocomplete.ListSelect2(url='brand-autocomplete'), required=False,)
 
    
    item_size = autocomplete.Select2ListCreateChoiceField(choice_list=Size.objects.all(), widget=autocomplete.ListSelect2(url='size-autocomplete', forward=['item_category', 'item_segment']),  required=False,)

    item_color = forms.CharField(required=False, disabled=True)

    colors = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), widget=autocomplete.ModelSelect2Multiple(url='color-autocomplete'), required=False)
    
    def get_firstassessment_choice_list():
        return ['Sale', 'Donation', 'Recycling']

    item_firstassessment = autocomplete.Select2ListChoiceField(choice_list=get_firstassessment_choice_list, widget=autocomplete.ListSelect2(url='firstassessment-autocomplete'))

    item_donationvalue = forms.DecimalField (min_value=0, decimal_places=2, required=False)

    def get_condition_choice_list():
        return ['New in a box', 'New w/o tags', 'New w tags', 'Like new', 'Gently used', 'Used', 'w defect']

    item_condition = autocomplete.Select2ListChoiceField(choice_list=get_condition_choice_list, widget=autocomplete.ListSelect2(url='condition-autocomplete'),required=False)

     # cut = forms.ModelMultipleChoiceField(
   #     queryset= Cut.objects.all(),
   #     widget=forms.CheckboxSelectMultiple(),
   # )

#    item_cut = autocomplete.Select2ListCreateChoiceField(choice_list=Cut.objects.all(), widget=autocomplete.ListSelect2(url='cut-autocomplete', forward=['itemtype']), required=False,)
    item_cut = forms.CharField(required=False, disabled=True)
    cuts =  forms.ModelMultipleChoiceField(queryset=Cut.objects.all(),widget=autocomplete.ModelSelect2Multiple(url='cut-autocomplete', forward=['itemtype']), required=False)
    item_style = forms.CharField(required=False, disabled=True)
    additional_info = forms.CharField(label='Additional information if necessary. Useful for unique items.', required=False, widget=forms.Textarea)

  #  item_fabric = autocomplete.Select2ListCreateChoiceField(choice_list=Fabric.objects.all(), widget=autocomplete.ListSelect2(url='fabric-autocomplete'), required=False, disabled=True)
    item_fabric = forms.CharField(required=False, disabled=True)
    
    item_usecase = forms.CharField(required=False, disabled=True)

    usecases = forms.ModelMultipleChoiceField(queryset=Usecase.objects.all(), widget=autocomplete.ModelSelect2Multiple(url='usecase-autocomplete'), required=False)

    item_postprice = forms.DecimalField (min_value=1, decimal_places=2, required=False,) 
    item_origprice = forms.DecimalField (min_value=1, decimal_places=2, required=False,) 

    def get_status_choice_list():
        return ['Ready4donation', 'Ready4sale', 'Ready4recycling', 'Donated', 'Up4sale', 'Ready2ship', 'Shipped', 'Recycled', 'Treatment', 'Returned']
    
    item_status = autocomplete.Select2ListCreateChoiceField(choice_list=get_status_choice_list, widget=autocomplete.ListSelect2(url='status-autocomplete'))
    
    item_statuschangedate = forms.DateField(label='Status Changed', initial=datetime.date.today)
    item_location =  forms.CharField(required=False,)

    def get_mktplace_choice_list():
        return ['Up', 'Down', 'Sold', 'Returned']
    
    ebay = autocomplete.Select2ListChoiceField(choice_list=get_mktplace_choice_list, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'), required=False,)
    poshmark = autocomplete.Select2ListChoiceField(choice_list=get_mktplace_choice_list, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'), required=False,)
    vinted = autocomplete.Select2ListChoiceField(choice_list=get_mktplace_choice_list, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'), required=False,)
    tradesy = autocomplete.Select2ListChoiceField(choice_list=get_mktplace_choice_list, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'), required=False,)
    craigslist = autocomplete.Select2ListChoiceField(choice_list=get_mktplace_choice_list, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'), required=False,)
    letgo = autocomplete.Select2ListChoiceField(choice_list=get_mktplace_choice_list, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'), required=False,)
    offerup = autocomplete.Select2ListChoiceField(choice_list=get_mktplace_choice_list, widget=autocomplete.ListSelect2(url='mktplace-autocomplete'), required=False,)
    offline = forms.ChoiceField(choices=[('',None),(1,'Sold')], required=False,) 
    
    def clean(self):
        cleaned_data = self.cleaned_data
        item_category = cleaned_data.get("item_category")
        db_value = Category.objects.get(category=item_category).category
        
        # if  db_value=='Clothes' or db_value=='Shoes' or db_value=='Accessories':
        #     # Keep the database consistent. The user may have
        #     # submitted a shipping_destination even if shipping
        #     # was not selected
        #     #self.cleaned_data['item_brand'] = ''
        #     if not cleaned_data['item_brand'] or not cleaned_data['item_size'] or not cleaned_data['item_color']:
        #         raise forms.ValidationError("'item_brand', 'item_size', and 'item_color' are required.")
        # else:
        #     cleaned_data['item_brand'] = ''
        #     cleaned_data['item_size'] = ''
        #     cleaned_data['item_color'] = ''

        if not cleaned_data['item_type']:
            if  db_value=='Clothes' or db_value=='Shoes' or db_value=='Accessories' or db_value=='Electronics' or db_value=='Toys' or db_value=='Home' or db_value=='SportsGear' or db_value=='Cosmetics':
                raise forms.ValidationError("'item_type' is required.")

        if not cleaned_data['item_brand']:
            if  db_value=='Clothes' or db_value=='Shoes' or db_value=='Accessories' or db_value=='Electronics' or db_value=='Toys' or db_value=='Home' or db_value=='SportsGear' or db_value=='Cosmetics':
                raise forms.ValidationError("'item_brand' is required.")
            
        if not cleaned_data['item_size']:
            if  db_value=='Clothes' or db_value=='Shoes':
                raise forms.ValidationError("'item_size' is required.")

      #  item_color=cleaned_data.get('item_color')
      #  item_color1=cleaned_data['item_color']
      #  color = Color.objects.get(color=item_color1).color
        if not cleaned_data['item_color']:
            if  db_value=='Clothes' or db_value=='Shoes':
                raise forms.ValidationError("'item_color' is required.")

        return self.cleaned_data




    def __init__(self, *args, **kwargs):
        super(InventoryitemForm, self).__init__(auto_id=True, *args, **kwargs)
     #   qs = Segment.objects.filter(category_id=InventoryitemForm.item_category)
     #   self.fields['item_segment'].queryset = Segment.objects.filter(category_id=self.instance.item_category)
        #    self.old_status = self.status
        

   # def to_python(self, value):
   #     if value in self.empty_values:
   #         return None
   #     try:
   #         key = self.to_field_name or 'pk'
   #         value = self.queryset.filter(category_id='Clothes').get(**{key: value})
   #     except (ValueError, TypeError, self.queryset.model.DoesNotExist):
   #         raise ValidationError(self.error_messages['invalid_choice'], code='invalid_choice')
   #     return value

    # def clean(self, value):
    # if value:
    #     lookup = get_lookup(self.channel)
    #     objs = lookup.get_objects( [value] )
    #     if objs:
    #         return objs[0]
    #     else:
    #         firstname, surname = value.split(" ")
    #         gender = self.channel.split("_")[0]
    #         new_skater = Skater(name=firstname, surname=surname, gender=gender)
    #         return new_skater
    # else:
    #     if self.required:
    #         raise forms.ValidationError(self.error_messages['required'])
    #     return None
    
    #def save(self, *args, **kwargs):
      #  qs = Segment.objects.filter(category_id="Clothes")
      #  self.fields['item_segment'].queryset = qs
      #  super(InventoryitemForm, self).save(*args, **kwargs)
    #      if self.old_status != self.status:
  #          self.statuschangedate = datetime.now()
    
   # def clean_name(self):
        # do something that validates your data
   #     cleaned_data = super(InventoryitemForm, self).clean()
        #firstassessment = cleaned_data.get("firstassessment")

        #return self.cleaned_data["name"]
    #if firstassessment == 'Sale':
     #   raise forms.ValidationError("A venue is required for events")




    #    image = forms.FileField(required=False, widget=forms.FileInput)
    # widget=autocomplete.ModelSelect2Multiple(url='cut-autocomplete')

  
