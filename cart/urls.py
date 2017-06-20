
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addToBasket/(?P<strain_pk>\d+)/$', views.add_to_basket, name = 'add_to_basket'),   
]