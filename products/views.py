from rest_framework import viewsets
from rest_framework.decorators import action
from products.serializers import ProductSerializer, AmountSerializer
from products.models import Product
from cart.models import CartProduct
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ProductModelViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(permission_classes=[IsAuthenticated, ],
            methods=['post', 'delete', ], detail=True,
            serializer_class=AmountSerializer)
    def cart(self, request, *args, **kwargs):
        cart = request.user.cart
        product = self.get_object()

        serializer = AmountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        requested_amount = serializer.validated_data.get('amount')

        if request.method == 'POST':

            if requested_amount > product.amount:
                return Response({'error': 'Requested amount is larger than product amount'},
                                 status=status.HTTP_400_BAD_REQUEST)
            
            product.amount -= requested_amount
            product.save()

            cart_product, created = CartProduct.objects.get_or_create(
                cart=cart,
                product=product,
            )
            if created:
                cart_product.amount = requested_amount
            else:
                cart_product.amount += requested_amount
            cart_product.save()

            return Response({'success': True})

        elif request.method == 'DELETE':
            
            if CartProduct.objects.filter(cart=cart, product=product).exists():
                cart_product = CartProduct.objects.get(product=product, cart=cart)

                if requested_amount > cart_product.amount:
                    return Response({'error': 'Requested amount is larger than product amount'},
                                    status=status.HTTP_400_BAD_REQUEST)
                elif requested_amount == cart_product.amount:
                    cart_product.delete()
                    return Response({'success': True})

                cart_product.amount -= requested_amount
                cart_product.save()
                return Response({'success': True})

            return Response({'error': 'Current cart does not contain this product'},
                            status=status.HTTP_400_BAD_REQUEST)


    # @action(permission_classes=[IsAuthenticated, ], methods=['post', 'delete'], detail=True)
    # def cart(self, request, *args, **kwargs):
    #     product = self.get_object()
    #     cart = request.user.cart

    #     if request.method == 'POST':
    #         cart.products.add(product)

    #     elif request.method == 'DELETE':
    #         cart.products.remove(product)

    #     return Response({'success': True})