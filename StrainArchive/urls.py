
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^management/', include('management.urls', namespace = "management")),
    url(r'^', include('userprofile.urls', namespace = "userprofile"))
]
