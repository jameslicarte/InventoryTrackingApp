from django.db import models


class Product(models.Model):
    prodType = models.CharField(max_length=255, default=None)
    product_name = models.CharField(max_length=255, default=None)
    field1 = models.CharField(max_length=255, default=None)
    field1_lbl = models.CharField(max_length=3, default=None)
    field2 = models.CharField(max_length=255, default=None)
    field2_lbl = models.CharField(max_length=3, default=None)
    field3 = models.CharField(max_length=255, default=None)
    field3_lbl = models.CharField(max_length=3, default=None)
    stock = models.IntegerField(default=None)

    def __str__(self):
        return self.product_name

class ProductType(models.Model):
    prodType = models.CharField(max_length=255)
    field1 = models.CharField(max_length=255) 
    field2 = models.CharField(max_length=255) 
    field3 = models.CharField(max_length=255) 
