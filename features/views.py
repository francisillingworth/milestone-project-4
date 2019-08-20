from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Feature, Comment
from .forms import NewFeatureForm, NewCommentForm, MakePaymentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe

# Create your views here.
def all_features(request):
    features= Feature.objects.all()
    features = sorted(features, key=lambda feature: feature.likes.count(), reverse=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(features, 3)
    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
    
    comments= Comment.objects.all()
    new_comment_form = NewCommentForm
    
    
    
    if request.method == "POST":
        new_comment_form = NewCommentForm(request.POST)
        feature = Feature.objects.get(id=request.POST["feature"])
        
        messages.success(request, "Your comment has been posted!")
        
        if new_comment_form.is_valid():
            
            
            
            instance = new_comment_form.save(commit=False)
            instance.feature = feature
            instance.author = request.user
            instance.save()
            
    
        
    return render(request,"features.html", {"features":features, "new_comment_form": new_comment_form, "comments":comments})
    
    
def NewFeature(request):
    
    if request.method == "POST":
        new_feature_form = NewFeatureForm(request.POST)
        messages.success(request, "Your feature has been posted!")
        
        if new_feature_form.is_valid():
            
            
            
            instance = new_feature_form.save(commit=False)
            instance.author = request.user
            instance.save()
            
            
    new_feature_form = NewFeatureForm()
    return render(request, 'new_feature.html', {"new_feature_form": new_feature_form})
    
    
    
def NewComment(request):
    
    if request.method == "POST":
        new_comment_form = NewCommentForm(request.POST)
        messages.success(request, "Your comment has been posted!")
        
        if new_comment_form.is_valid():
            
            
            
            instance = new_comment_form.save(commit=False)
            instance.author = request.user
            instance.save()
            
            
    new_comment_form = NewCommentForm()
    return render(request, 'add_comment.html', {"new_comment_form": new_comment_form})

def like_feature(request):
    feature = get_object_or_404(Feature, id=request.POST.get('feature_id'))
    messages.success(request, "Thank you for liking this feature, to confirm this Like please complete the payment form below. Remember the features with the highest number of likes will be worked on first!")
    feature.likes.add(request.user)
    return redirect(reverse('checkout'))
    
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        payment_form = MakePaymentForm(request.POST)

        if payment_form.is_valid():
            
            try:
                customer = stripe.Charge.create(
                    amount=1000,
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                return redirect(reverse('features'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        
    
    return render(request, "checkout.html", { "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
