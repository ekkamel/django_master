from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),    # r refers to root  ^ is the domain address
    url(r'', include('main.urls')), 
]
