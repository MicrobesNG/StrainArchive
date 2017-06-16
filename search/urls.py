from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.search, name = 'search'),
    url(r'^post/(?P<strain_pk>\d+)/$', views.details, name = 'details'),
    url(r'^results/(?P<parameterString>.+)/$', views.results, name = 'results')
]