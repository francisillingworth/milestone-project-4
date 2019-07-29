from django import forms
from issues.models import Issue
from django.core.exceptions import ValidationError

class NewIssueForm():
    """Form to add new issue"""
    issue_name = forms.CharField(widget=forms.Textarea,)
    issue_description = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Issue
        fields = ['issue_name' , 'issue_description']
    
