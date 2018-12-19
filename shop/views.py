from django.shortcuts import render
from .models import Menus
from.models import Orders

# Create your views here.


def home(request):


   menus = Menus.objects.all()[:5] # get the first 10 menus

   context = {
     'menus': menus
   }

   return render(request, 'home.html', context)



