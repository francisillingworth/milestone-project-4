from django.shortcuts import render
from .models import Issue
from issues.forms import NewIssueForm


# Create your views here.
def all_issues(request):
    issues= Issue.objects.all()
    return render(request,"issues.html", {"issues":issues})
    
    
def NewIssue(request):
    new_issue_form = NewIssueForm
    return render(request, 'issues.html', {"new_issue_form": new_issue_form})