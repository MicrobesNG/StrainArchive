from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^search/', views.search, name = 'search'),
    url(r'^post/(?P<strain_pk>\d+)/$', views.details, name = 'details'),
    url(r'^results/$', views.results, name = 'results')
]