from django.shortcuts import render
from data_crawl.models import Product_details as pd, Product_type

# Create your views here.
def index(request):
    p = pd.objects.all()
 
    return render(request, 'index.html', {'product': p})

