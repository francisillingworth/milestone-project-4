from django import forms
from .models import Issue
from django.core.exceptions import ValidationError

class NewIssueForm(forms.ModelForm):
    """Form to add new issue"""
    name = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Issue
        fields = ['name' , 'description']
        

        
    
