from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name = 'search'),
    url(r'^strain/(?P<strain_pk>\d+)/$', views.details, name = 'details'),
    url(r'^results/(?P<page_number>\d+)/$', views.results, name = 'results'),
    url(r'^updateBasket/(?P<strain_pk>\d+)/$', views.details, name = 'update_basket'),
]