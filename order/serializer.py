from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'type', 'cart', 'total_amount', 'products', ]
        read_only_fields = ['total_amount', 'products', ]

    def get_products(self, instance):
        result_data = []
        for product in instance.ordered_products.all():
            data = {
                'id': product.product_id,
                'name': product.product.name,
                'amount': product.id,
            }
            result_data.append(data)
        return result_data


    def update(self, instance, validated_data):
        if instance.type = Order.OrderType.PENDING and validated_data['type'] == 'canceled':
            ordered_products = instance.order_products.all()
            for ordered_product in ordered_products:
                ordered_product.product.amount += ordered_product.amount
                ordered_product.product.save()
        return super().update(instance, validated_data)
