from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'shop/home.html')


def contact(request):
    return render(request, 'shop/contact.html')


def galary(request):
    return render(request, 'shop/galary.html')


def menus(request):
    return render(request, 'shop/menus.html')


def order(request):
    return render(request, 'shop/order.html')




