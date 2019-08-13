from django.conf.urls import url, include
from .views import all_features, NewFeature, NewComment



urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^NewFeature/$', NewFeature, name='NewFeature'),
    url(r'^NewComment/$', NewComment, name='NewComment'),
]