from django import forms
from .models import Feature, Comment
from django.core.exceptions import ValidationError

class NewFeatureForm(forms.ModelForm):
    """Form to add new issue"""
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'(100 characters max)'}), max_length="100")
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Feature
        fields = ['name' , 'description']
        
        
class NewCommentForm(forms.ModelForm):
    """Form to add comment"""
    
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control commentLabel' ,'placeholder':'(300 characters max)'}), label="Enter a comment", max_length=300)
    
    class Meta:
        model = Comment
        fields = ['comment']
        
class MakePaymentForm(forms.Form):
    
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Expiry Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Expiry Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
        