
from django.conf.urls import url, include
from django.contrib import admin
from shop import views as v


urlpatterns = [
    # admin page url
    url(r'^admin/', admin.site.urls),

    # home page url
    url(r'^$', v.home),

    # Contact us page url
    url(r'^contact/', v.contact),

    #  galary page url

    url(r'^galary/', v.galary),

    #  menus page url

    url(r'^menus/', v.menus),

    # make order page url

    url(r'^order/', v.order),
]
