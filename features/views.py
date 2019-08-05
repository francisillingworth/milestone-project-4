from django.shortcuts import render
from django.contrib import messages
from .models import Feature
from .forms import NewFeatureForm

# Create your views here.
def all_features(request):
    features= Feature.objects.all()
    return render(request,"features.html", {"features":features})
    
def NewFeature(request):
    
    if request.method == "POST":
        new_feature_form = NewFeatureForm(request.POST)
        messages.success(request, "Your feature has been posted!")
        
        if new_feature_form.is_valid():
            new_feature_form.save()
            
            
    new_feature_form = NewFeatureForm()
    return render(request, 'new_feature.html', {"new_feature_form": new_feature_form})