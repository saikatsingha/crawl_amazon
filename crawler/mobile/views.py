from django.shortcuts import render
from data_crawl.models import Product_details, Product_type

# Create your views here.
def index(request):

    product = Product_details.objects.all()
    # context = {
    #     'product': product,
    #     'company_name': company_name, 
    #     'photo': photo, 
    #     'description': description, 
    #     'price': price,
    #     'memory': memory, 
    #     'display': display,
    #     'camera': camera, 
    #     'battery': battery, 
    #     'processor': processor)  
    # }
    # Subject: Subjectsnames.objects.get(id=id)

    # subjects_data: {
    #     "subjects_names":Subject
    # }
    context = {
        'product':product
    }
    print (product)
    return render(request, 'index1.html', context)

