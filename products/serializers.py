from rest_framework import serializers

from products.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'amount', 'rating']
        extra_kwargs = {'name': {'required': False}}


class AmountSerializer(serializers.Serializer):

    amount = serializers.IntegerField()
