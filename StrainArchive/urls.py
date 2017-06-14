
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^management/', include('management.urls', namespace = "management")),
    url(r'^user/', include('userprofile.urls', namespace = "userprofile")),
    url(r'^search/', include('search.urls', namespace = "search")),
    url(r'^', include('archive.urls', namespace = "archive"))
]
