from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.management_dashboard, name = "dashboard"),
    url(r'^strains', views.management_strains, name = "strains"),
    url(r'^sales', views.management_sales, name = "sales"),
    url(r'^users', views.management_users, name = "users"),
    url(r'^getQuoteDetails/(?P<quote_pk>\d+)/$', views.get_quote_details, name = "get_quote_details"),
    url(r'^getOrderDetails/(?P<order_pk>\d+)/$', views.get_order_details, name = "get_order_details"),
    url(r'^getPromoCodes/(?P<promo_pk>\d+)/$', views.get_promo_codes, name = "get_promo_codes"),
    url(r'^sendQuote/(?P<quote_pk>\d+)/$', views.send_quote, name = "send_quote"),
    url(r'^updateUserStatus/(?P<user_pk>\d+)/$', views.update_user_status, name = "update_user_status"),
    url(r'^login/', views.login, name = "login"),
    url(r'^logoutUser/', views.logout_user, name = "logout_user"),
]