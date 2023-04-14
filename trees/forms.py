from django.forms import ModelForm, DateInput
from django.forms.widgets import SelectDateWidget
from .models import Tree
from django import forms

class TreeRecordForm(ModelForm):
    harvestDate = forms.DateField(widget=SelectDateWidget)
    harvestTime = forms.TimeField(widget=DateInput(attrs={'type': 'time'}))

    class Meta:
        model = Tree
        fields = ["section", "age", "variety", "soil_moisture", "temperature",
                  "humidity", "light_exposure", "nutrient_levels", "pest_disease_outbreaks",
                  "harvestTime", "harvestDate", "tree_image"]
