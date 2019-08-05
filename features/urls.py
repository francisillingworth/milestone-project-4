from django.conf.urls import url, include
from .views import all_features, NewFeature

urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^NewFeature/$', NewFeature, name='NewFeature'),
]
