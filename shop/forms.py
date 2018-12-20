# create forms from the existing models

from django.forms import ModelForm
from .models import Orders


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        exclude = ['created_at']  # include all fields except the created_at filed




