from django import forms
from django.forms import ModelForm
from .models import Verification

class UploadForm(ModelForm):
    id_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter 6-digit ID number'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter item category'}))

    class Meta:
        model = Verification
        fields = ["id_num", "category", "form"]