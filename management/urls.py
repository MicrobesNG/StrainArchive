from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.management_dashboard, name = "dashboard"),
    url(r'^strains', views.management_strains, name = "strains"),
    url(r'^sales', views.management_sales, name = "sales"),
    url(r'^users', views.management_users, name = "users")
]