from django.db import models
from datetime import datetime   
USE_TZ=True
TIME_ZONE = 'Asia/Shanghai'


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
    updated_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.product_name


class ProductType(models.Model):
    prodType = models.CharField(max_length=255)
    field1_name = models.CharField(max_length=255) 
    field2_name = models.CharField(max_length=255, blank=True) 
    field3_name = models.CharField(max_length=255, blank=True) 

