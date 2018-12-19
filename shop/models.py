from django.db import models
from datetime import datetime

# Create your models here.

# will create a database table called Menus


class Menus(models.Model):
    coffee_name = models.CharField(max_length=200)
    description = models.TextField()
    coffee_image = models.FileField(upload_to='coffee_images', blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

# will create a database table called orders


class Orders(models.Model):
    customer_name = models.CharField(max_length=20)
    customer_email = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=50)
    order_description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)


