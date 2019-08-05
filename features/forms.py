from django import forms
from .models import Feature
from django.core.exceptions import ValidationError

class NewFeatureForm(forms.ModelForm):
    """Form to add new issue"""
    name = forms.CharField(widget=forms.Textarea,)
    description = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Feature
        fields = ['name' , 'description']
    
