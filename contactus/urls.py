
from django.conf.urls import url
from .import views


urlpatterns = [
    url(r'^$', views.index, name='index')  # menus slash nothing is going to load the menus page
]

