
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addToBasket/(?P<strain_pk>\d+)/$', views.add_to_basket, name = 'add_to_basket'),
    url(r'^removeFromBasket/(?P<strain_pk>\d+)/$', views.remove_from_basket, name = 'remove_from_basket'),
    url(r'^checkout/', views.checkout, name = "checkout"),
    url(r'^clearBasket/', views.clear_basket, name = "clearBasket"),
    url(r'checkPromotion/(?P<promotion_code>[\w\-]+)/$', views.check_promotion, name = "check_promotion")
    url(r'cancelPromotion/(?P<promotion_code>[\w\-]+)/$', views.cancel_promotion, name = "cancel_promotion")
]