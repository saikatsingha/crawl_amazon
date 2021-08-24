from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
from data_crawl.models import Product_details

# Create your views here.

def index(request):
    
    page = requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy,4io&marketplace=FLIPKART&otracker=product_breadCrumbs_Mobiles")
    soup = bs(page.content, "html.parser")

    title = soup.title
    # print(type(soup))
    # print(type(title.string))
    #print(soup.title)
    #print (page.text)
    i = 0
    k = 0
    Name = []
    Ram = []
    Price = []
    Name = soup.find_all("div" , attrs={"class":"_4rR01T"})
    Price = soup.find_all("div" , attrs={"class":"_30jeq3 _1_WHN1"})
    Ram = soup.find_all("li", attrs={"class":"rgWa7D"})
    for k in range(0, len(Name)):
        p = Product_details(company_name = Name[k].get_text(), 
                             photo = '', 
                             description = Name[k].get_text(), 
                             price = Price[k].get_text().replace("₹",'').replace(",",'').strip(),
                             memory = Ram[i].get_text(), 
                             display = Ram[i+1].get_text(),
                             camera = Ram[i+2].get_text(), 
                             battery = Ram[i+3].get_text(), 
                             processor = Ram[i+4].get_text())

        i = i+6
        p.save()

    return render(request,'index.html')
