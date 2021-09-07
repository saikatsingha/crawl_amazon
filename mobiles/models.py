from django.db import models
from django.contrib import admin
from datetime import datetime

from django.db.models.deletion import DO_NOTHING



class Product_type(models.Model):
    product_nameId = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)

class Product_details(models.Model):
    Product_detailsId = models.AutoField(primary_key=True)
    product_type = models.ForeignKey(Product_type, blank=True, null=True, on_delete=DO_NOTHING)
    company_name = models.CharField(max_length=200, unique = True)
    price = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    memory = models.IntegerField(default=0)
    display = models.IntegerField(default=0)
    camera = models.IntegerField(default=0)
    battery = models.IntegerField(default=0)
    processor = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=200, blank=True)
