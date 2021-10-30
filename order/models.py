from django.db import models


class Order(models.Model):
    class OrderType(models.TextChoices):
        PENDING = 'pending'
        DELIVERED = 'delivered'
        CANCELED = 'canceled'
    type = models.CharField(max_length=128, choices=OrderType.choices,
                            default=OrderType.PENDING)
    cart = models.ForeignKey('cart.Cart', on_delete=models.SET_NULL, null=True,
                             related_name='orders')
    total_price = models.IntegerField()
    total_amount = models.IntegerField()
    products = models.ManyToManyField('products.Product', through='OrderProduct')


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE,
                                related_name='order_products')
    amount = models.IntegerField()
