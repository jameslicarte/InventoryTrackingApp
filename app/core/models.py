from django.db import models

class Product(models.Model):
    brand = models.CharField(max_length=255)
    brand_id = models.CharField(max_length=3)
    prodType = models.CharField(max_length=255)
    prodType_id = models.CharField(max_length=3)
    color = models.CharField(max_length=255)
    color_id = models.CharField(max_length=3)
    size = models.CharField(max_length=255)
    size_id = models.CharField(max_length=3)
    description = models.TextField()
    date_added = models.DateTimeField()
    stock = models.IntegerField()
