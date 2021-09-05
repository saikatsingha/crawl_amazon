from django.http.response import JsonResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse

from mobiles.models import Product_details, Product_type
from mobiles.serializers import Product_detailsSerializers, Product_typeSerializers

@csrf_exempt
def productApi(request, id=0):
    products = Product_details.objects.all()
    products_serializers = Product_detailsSerializers(products, many=True)
    return JsonResponse(products_serializers.data, safe=False)
