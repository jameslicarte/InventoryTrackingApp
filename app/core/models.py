from django.db import models


class Product(models.Model):
    prodType = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    field1 = models.CharField(max_length=255)
    field1_lbl = models.CharField(max_length=3, blank=True)
    field2 = models.CharField(max_length=255, blank=True)
    field2_lbl = models.CharField(max_length=3, blank=True)
    field3 = models.CharField(max_length=255, blank=True)
    field3_lbl = models.CharField(max_length=3, blank=True)
    stock = models.IntegerField(default='0')

    def __str__(self):
        return self.product_name

class ProductType(models.Model):
    prodType = models.CharField(max_length=255)
    field1_name = models.CharField(max_length=255) 
    field2_name = models.CharField(max_length=255) 
    field3_name = models.CharField(max_length=255) 
