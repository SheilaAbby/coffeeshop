from django.db import models
from datetime import datetime

# Create your models here.

# will create a database table called Menus


class Menus(models.Model):
    coffee_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    coffee_image = models.FileField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = 'menus'

    # defines the string to be used on the admin page
    def __str__(self):
        return '%s' % self.coffee_name
# will create a database table called orders


class Orders(models.Model):
    customer_name = models.CharField(max_length=20, blank=False)
    customer_email = models.CharField(max_length=200, blank=False)
    customer_address = models.CharField(max_length=50, blank=False)
    order_description = models.TextField(blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = 'orders'

    # defines the string to be used on the admin page
    def __str__(self):
        return '%s' % self.customer_name

