from django.shortcuts import render
from .forms import OrderForm
from .models import Menus
from django.contrib import messages


# Create your views here.


def home(request):
    menus = Menus.objects.all()[:5]  # get the first 10 menus
    form = OrderForm(request.POST)  # A form bound to the POST data
    if request.method == "POST":
        if form.is_valid(): # All Validation rules pass
            order_item = form.save(commit=False)
            order_item.save()  # save to the database
            messages.success(request, 'Success, Order sent!')

        else:
            form = OrderForm()  # unbound form

    context = {
            'menus': menus,
            'form': form
     }

    return render(request, 'shop.html', context)



