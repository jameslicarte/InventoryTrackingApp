from django.test import TestCase
from rest_framework import status

CREATE_PRODUCT_URL = ('http://127.0.0.1:8000/api/products/')


class PublicProductApiTest(TestCase):

    def test_api_product_create(self):
        """Test the products API"""
        prodType = 'T-Shirt'
        product_name = 'Levis'
        field1 = 'White'
        field2 = 'Small'
        field3 = 'Vneck'
        payload = {
            'prodType': prodType,
            'product_name': product_name,
            'field1': field1,
            'field2': field2,
            'field3': field3
        }
        
        res = self.client.post(CREATE_PRODUCT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
