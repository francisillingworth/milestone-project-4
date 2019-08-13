from django.conf.urls import url, include
from .views import all_issues, NewIssue, NewComment
from issues import views



urlpatterns = [
    url(r'^$', all_issues, name='issues'),
    url(r'^NewIssue/$', NewIssue, name='NewIssue'),
    url(r'^NewComment/$', NewComment, name='NewComment'),
    url(r'^like/$', views.like_issue, name='like_issue'),
]