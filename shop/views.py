from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def galary(request):
    return render(request, 'galary.html')


def menus(request):
    return render(request, 'menus.html')


def order(request):
    return render(request, 'order.html')




