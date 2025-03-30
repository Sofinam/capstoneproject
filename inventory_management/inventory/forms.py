from django import forms
from .models import Inventory
from django.forms import DateTimeField

class InventoryForm(forms.ModelForm):
    date_display = DateTimeField(disabled=True, required=False, label='Date Added', initial=None)
    class Meta:
        model = Inventory
        fields = ['Name','Description', 'Quantity', 'Price', 'Category']