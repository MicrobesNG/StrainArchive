from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_page, name = "login"),
    url(r'^dashboard/', views.user_dashboard, name = "dashboard"),
]