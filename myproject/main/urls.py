from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^bath/$', views.bath, name='bath'),
]