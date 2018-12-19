
from django.conf.urls import url, include
from django.contrib import admin
from shop import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # admin page url
    url(r'^admin/', admin.site.urls),

    # home page url
    url(r'^$', v.home),
]

urlpatterns += staticfiles_urlpatterns()



