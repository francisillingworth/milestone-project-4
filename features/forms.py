from django import forms
from features.models import Feature
from django.core.exceptions import ValidationError

class NewFeatureForm():
    """Form to add new issue"""
    feature_name = forms.CharField(widget=forms.Textarea,)
    feature_description = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Feature
        fields = ['feature_name' , 'feature_description']
    
