
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^menus/', include('menus.urls')),
    url(r'^galary/', include('coffeegalary.urls')),
    url(r'^order/', include('orders.urls')),
    url(r'^contact/', include('contactus.urls')),
]
