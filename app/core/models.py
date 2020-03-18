from django.db import models


class Product(models.Model):
    brand = models.CharField(max_length=255, default=None)
    brand_id = models.CharField(max_length=3, default=None)
    prodType = models.CharField(max_length=255, default=None)
    prodType_id = models.CharField(max_length=3, default=None)
    color = models.CharField(max_length=255, default=None)
    color_id = models.CharField(max_length=3, default=None)
    size = models.CharField(max_length=255, default=None)
    size_id = models.CharField(max_length=3, default=None)
    description = models.TextField(default=None)
    date_added = models.DateTimeField(default=None)
    stock = models.IntegerField(default=None)
