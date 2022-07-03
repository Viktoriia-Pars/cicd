from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

class TestProducts(TestCase):
    def setUp(self) -> None:
        self.payload = {'id':4,
                        'name': 'Apple IPhone 13',
                        'price': 50500,
                        'release_date': '05-05-2022'}

    def test_create_product_without_id(self):
        data = self.payload.copy()
        data.pop('id')
        client = APIClient()
        url = reverse('create-phone')
        response = client.post(url, data)
        self.assertEqual(response.status_code, 400)

    def test_create_product_without_name(self):
        data = self.payload.copy()
        data.pop('name')
        client = APIClient()
        url = reverse('create-phone')
        response = client.post(url, data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('name', response.data)