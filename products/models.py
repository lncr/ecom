from django.db import models

# Create your models here.

class Product(models.Model):
    category = models.ForeignKey('category.Category', on_delete=models.SET_NULL,
                                 related_name='products', null=True)
    name = models.CharField(max_length=128)
    amount = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
