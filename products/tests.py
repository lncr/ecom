from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Product


User = get_user_model()


class ProductsTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test1234')
        self.product1 = Product.objects.create(name='Apple', amount=100, price=50)
        self.product2 = Product.objects.create(name='Notebook', amount=5, price=1000)

    def test_list_products(self):
        url = reverse('product-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_cart_adding_unauthorized(self):
        url = reverse('product-cart', kwargs={'pk': self.product1.id})
        data = {'amount': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cart_adding_authorized(self):
        url = reverse('product-cart', kwargs={'pk': self.product1.id})
        data = {'amount': 5}
        self.client.force_authenticate(self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
