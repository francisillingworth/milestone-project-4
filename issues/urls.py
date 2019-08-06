from django.conf.urls import url, include
from .views import all_issues, NewIssue, NewComment



urlpatterns = [
    url(r'^$', all_issues, name='issues'),
    url(r'^NewIssue/$', NewIssue, name='NewIssue'),
    url(r'^NewComment/$', NewComment, name='NewComment'),
]