from django.shortcuts import render
from .models import Feature
from .forms import NewFeatureForm

# Create your views here.
def all_features(request):
    features= Feature.objects.all()
    return render(request,"features.html", {"features":features})
    
def NewFeature(request):
    new_feature_form = NewFeatureForm()
    print(new_feature_form)
    return render(request, 'features.html', {"new_feature_form": new_feature_form})