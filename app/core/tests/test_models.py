from django.test import TestCase
from core.models import Product


class ModelTest(TestCase):
    def test_create_new_product_successful(self):
        """Test create new product is succesful"""
        brand = 'LEVIS'
        product_id = 4
        product_obj = Product(
            brand=brand,
            id=product_id
        )

        self.assertEqual(product_obj.brand, brand)
        self.assertEqual(product_obj.id, product_id)
    # def test_product_quantity_recieved_added_to_inventory_successful(self):
    #     """Test product quantity received added to inventory successful"""
    # def test_product_deduct_in_inventory_successful(self):
    #     """Test product shiped quantity deducted in inventory successful"""
