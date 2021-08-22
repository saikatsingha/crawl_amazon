from django.contrib import admin

# Register your models here.
from .models import Product_type
from .models import Product_details

admin.site.register(Product_type)
admin.site.register(Product_details)
