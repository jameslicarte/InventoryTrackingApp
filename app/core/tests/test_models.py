from django.test import TestCase
from core.models import Product, ProductType


class ModelTests(TestCase):

    def test_create_new_product_successful(self):
        """Test create new product is succesful"""
        prodType = 'T-Shirt'
        product_name = 'Levis'
        field1 = 'White'
        field2 = 'Small'
        field3 = 'Vneck'
        stock = 0
        product_obj = Product(
            prodType=prodType,
            product_name=product_name,
            field1=field1,
            field2=field2,
            field3=field3,
            stock=stock
        )

        self.assertEqual(product_obj.prodType, prodType)
        self.assertEqual(product_obj.product_name, product_name)
        self.assertEqual(product_obj.field1, field1)
        self.assertEqual(product_obj.field2, field2)
        self.assertEqual(product_obj.field3, field3)
        self.assertEqual(product_obj.stock, stock)
        
    def test_create_new_product_type_successful(self):
        """Test create new product type is succesful"""
        prodType = 'T-Shirt'
        field1_name = 'Color'
        field2_name = 'Type'
        field3_name = 'Size'
        product_obj = ProductType(
            prodType=prodType,
            field1_name=field1_name,
            field2_name=field2_name,
            field3_name=field3_name
        )

        self.assertEqual(product_obj.prodType, prodType)
        self.assertEqual(product_obj.field1_name, field1_name)
        self.assertEqual(product_obj.field2_name, field2_name)
        self.assertEqual(product_obj.field3_name, field3_name)
