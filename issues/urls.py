from django.conf.urls import url, include
from .views import all_issues, NewIssue



urlpatterns = [
    url(r'^$', all_issues, name='issues'),
    url(r'^issues/$', NewIssue, name='NewIssue'),
]