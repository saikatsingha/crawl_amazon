from rest_framework import serializers
from mobiles.models import Product_details, Product_type

class Product_typeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product_type
        fields = ('product_typeId',
                  'product_name')

class Product_detailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product_details
        fields = ('Product_detailsId',
                  'product_type',
                  'company_name',
                  'price',
                  'photo',
                  'memory',
                  'display',
                  'camera',
                  'battery',
                  'processor')