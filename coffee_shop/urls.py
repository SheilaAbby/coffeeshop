
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    # admin page url
    url(r'^admin/', admin.site.urls),

    # home page url
    url(r'^$', include('shop.urls.home')),
    url(r'^menus/', include('shop.urls.menus')),
    url(r'^galary/', include('shop.urls.galary')),
    url(r'^order/', include('shop.urls')),
    url(r'^contact/', include('shop.urls')),
]
