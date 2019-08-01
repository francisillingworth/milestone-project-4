from django.shortcuts import render
from .models import Issue
from .forms import NewIssueForm


# Create your views here.
def all_issues(request):
    issues= Issue.objects.all()
    return render(request,"issues.html", {"issues":issues})
    
    
def NewIssue(request):
    new_issue_form = NewIssueForm()
    print(new_issue_form)
    return render(request, 'issues.html', {"new_issue_form": new_issue_form})
    