from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Issue, Comment
from .forms import NewIssueForm, NewCommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def all_issues(request):
    issues= Issue.objects.all()
    issues = sorted(issues, key=lambda issue: issue.likes.count(), reverse=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(issues, 3)
    try:
        issues = paginator.page(page)
    except PageNotAnInteger:
        issues = paginator.page(1)
    except EmptyPage:
        issues = paginator.page(paginator.num_pages)

    comments= Comment.objects.all()
    new_comment_form = NewCommentForm
    
    
    
    if request.method == "POST":
        new_comment_form = NewCommentForm(request.POST)
        issue = Issue.objects.get(id=request.POST["issue"])
        
        messages.success(request, "Your comment has been posted!")
        
        if new_comment_form.is_valid():
            
            
            
            instance = new_comment_form.save(commit=False)
            instance.issue = issue
            instance.author = request.user
            instance.save()
            
    
        
    return render(request,"issues.html", {"issues":issues, "new_comment_form": new_comment_form, "comments":comments})
    
    
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
    
    
    
def like_issue(request):
    issue = get_object_or_404(Issue, id=request.POST.get('issue_id'))
    messages.success(request, "Thank you for liking this issue, the issues with the most likes will be worked on first!")
    issue.likes.add(request.user)
    return redirect(reverse('issues'))
    
    