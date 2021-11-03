from django.db.models import Max, Sum, Avg
from rest_framework import serializers

from products.models import Product


def generate_name():
    number = Product.objects.aggregate(Avg('id')) + 1
    return f'Product#{number['id__max']}'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'amount', ]
        extra_kwargs = {'name': {'required': False}}

    def create(self, validated_data):
        if not validata_data.get('name'):
            name = generate_name()
            validated_data['name'] = name
        return super().create(validated_data)

    def update(self, instance, validated_data):
        pass
    
    def delete(self, instance):
        pass

# api/v1/products/<id>/     PATCH / PUT    DELETE    GET


# retrieve
# list
# create
# update
# delete



class AmountSerializer(serializers.Serializer):

    amount = serializers.IntegerField()
