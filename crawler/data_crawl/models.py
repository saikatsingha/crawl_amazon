from django.db import models
from datetime import datetime


class Product_type(models.Model):
  product_name = models.CharField(max_length=200)

  def __str__(self):
    return self.name



class Product_details(models.Model):
  company_name = models.CharField(max_length=200)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  description = models.TextField(blank=True)
  memory = models.CharField(max_length=100)
  display = models.CharField(max_length=100)
  camera = models.CharField(max_length=100)
  battery = models.CharField(max_length=100)
  processor = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name