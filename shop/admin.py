from django.contrib import admin

# Register your models here.
from .models import Menus
from .models import Orders

admin.site.register(Menus)

admin.site.register(Orders)
