
from django.conf.urls import url
from .import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^$', views.contact, name='contact'),
    url(r'^$', views.galary, name='galary'),
    url(r'^$', views.menus, name='menus'),
    url(r'^$', views.order, name='order')

]

