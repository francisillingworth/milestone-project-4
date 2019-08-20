from django.conf.urls import url, include
from .views import all_features, NewFeature, NewComment, checkout
from features import views


urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^NewFeature/$', NewFeature, name='NewFeature'),
    url(r'^NewComment/$', NewComment, name='NewComment'),
    url(r'^like/$', views.like_feature, name='like_feature'),
    url(r'^checkout$', checkout, name='checkout'),
]