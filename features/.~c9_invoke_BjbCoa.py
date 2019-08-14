from django import forms
from .models import Feature, Comment
from django.core.exceptions import ValidationError

class NewFeatureForm(forms.ModelForm):
    """Form to add new issue"""
    name = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),)
    
    class Meta:
        model = Feature
        fields = ['name' , 'description']
        
        
class NewCommentForm(forms.ModelForm):
    """Form to add comment"""
    
    #comment = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Comment
        fields = ['comment']
        