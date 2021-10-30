from rest_framework import mixins, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from orders.models import Order, OrderProduct



class OrderView(mixins.CreateMixin,
                mixins.RetrieveMixin,
                mixins.ListMixin,
                mixins.UpdateMixin,
                GenericAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerialzier
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(cart=self.request.user.cart)

    def create(self, request, *args, **kwargs):
        cart = request.user.cart
        if not cart.products.all().exists():
            return Response({'error': True, 'message': 'You have no products in cart'}
                            status=status.HTTP_404_NOT_FOUND)
        order = Order.objects.create()

        for obj in cart.cart_products.all():
            OrderProduct.objects.create(order=order, product=obj.product, amount=obj.amount)
        cart.products.clear()
        serializer = self.get_serialzier(instance=order)
        return Response(serialzier.data)
