from django.db import models


class Order(models.Model):
    cart = models.ForeignKey('cart.Cart', on_delete=models.SET_NULL, null=True,
                             related_name='orders')
    total_price = models.IntegerField()
    total_amount = models.IntegerField()
    products_list = models.TextField()
