from django.db import models


class Product(models.Model):
    """Product model"""
    sku = models.CharField(max_length=15)
    description = models.TextField()
    date_added = models.DateTimeField()
    stock = models.IntegerField()
