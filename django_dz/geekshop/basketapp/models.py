from django.db import models
from authapp.models import ShopUser
from mainapp.models import Product
from django.conf import settings


# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)
