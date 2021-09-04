from django.db import models
from datetime import datetime

from django.db.models.deletion import DO_NOTHING



class Product_type(models.Model):
    product_nameID = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.product_name



class Product_details(models.Model):
    Product_detailsID = models.AutoField(primary_key=True)
    product_type = models.ForeignKey(Product_type, blank=True, null=True, on_delete=DO_NOTHING)
    company_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    memory = models.CharField(max_length=100, blank=True)
    display = models.CharField(max_length=100, blank=True)
    camera = models.CharField(max_length=100, blank=True)
    battery = models.CharField(max_length=100, blank=True)
    processor = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.company_name