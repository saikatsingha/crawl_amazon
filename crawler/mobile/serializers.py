from rest_framework import serializars
from data_crawl.models import Product_details, Product_type

class Product_typeSerializars(serializars.ModelSerializars):
    class Meta:
        model = Product_type
        fields = ('product_typeId',
                  'product_name')

class Product_detailsSerializars(serializars.ModelSerializars):
    class Meta:
        model = Product_details
        fields = ('product_detailsId',
                  'product_type',
                  'company_name',
                  'description',
                  'price',
                  'photo',
                  'memory',
                  'display',
                  'camera',
                  'battery',
                  'processor')