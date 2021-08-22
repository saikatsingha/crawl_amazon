from django.db import models
from datetime import datetime

from django.db.models.deletion import DO_NOTHING



class Product_type(models.Model):
    product_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.product_name



class Product_details(models.Model):    
    product_type = models.ForeignKey(Product_type, blank=True, null=True, on_delete=DO_NOTHING)
    company_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    memory = models.CharField(max_length=100)
    display = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name