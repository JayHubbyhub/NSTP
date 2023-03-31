from django.forms import ModelForm, DateInput
from django.forms.widgets import SelectDateWidget
from .models import Item
from django import forms

class ItemForm(ModelForm):
    dateFound = forms.DateField(widget=SelectDateWidget)
    timeFound = forms.TimeField(widget=DateInput(attrs={'type': 'time'}))

    class Meta:
        model = Item
        fields = ["category", "description", "locationFound", "dateFound", "timeFound", "lost_item_image"]
