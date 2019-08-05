from django.shortcuts import render
from django.contrib import messages
from .models import Issue
from .forms import NewIssueForm


# Create your views here.
def all_issues(request):
    issues= Issue.objects.all()
    return render(request,"issues.html", {"issues":issues})
    
    
def NewIssue(request):
    
    if request.method == "POST":
        new_issue_form = NewIssueForm(request.POST)
        messages.success(request, "Your issue has been posted!")
        
        if new_issue_form.is_valid():
            
            
            
            instance = new_issue_form.save(commit=False)
            instance.author = request.user
            instance.save()
            
            
    new_issue_form = NewIssueForm()
    return render(request, 'new_issue.html', {"new_issue_form": new_issue_form})
    
