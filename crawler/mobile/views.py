from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from MobileApp.models import Product_details, Product_type
from MobileApp.serializars import Product_detailsSerializars, Product_typeSerializars



# Create your views here.
def index(request):
    p = pd.objects.all()
 
    return render(request, 'index.html', {'product': p})

