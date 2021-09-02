# import _typeshed
import requests
from bs4 import BeautifulSoup as bs
import shutil 
import psycopg2
import cv2 
import os 

# Create your views here.


page = requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree")
soup = bs(page.content, "html.parser")

i = 0
k = 0
Name = []
Ram = []
Image = []
Price = []
path  = []
Name = soup.find_all("div" , attrs={"class":"_4rR01T"})
Price = soup.find_all("div" , attrs={"class":"_30jeq3 _1_WHN1"})
Ram = soup.find_all("li", attrs={"class":"rgWa7D"})
Image = soup.find_all("img", attrs={"class":"_396cs4 _3exPp9"})

for k in range(len(Name)):
    
    print(Image[k+0].get("src"))
    print(Image[k+1].get("src"))
    print(Image[k+2].get("src"))
    print(Image[k+3].get("src"))
    print("\n")
    print("\n")


#     # i = i+6
#     # p.save()

#     # path = Image[k+4].get("src")
#     # img = cv2.imread(path)
#     # d = 'home/saikat/python_projects/image'
#     # img = cv2.imread(path) 
#     # os.chdir(directory) 
#     # print(os.listdir(directory))  
#     filename = Name[k].get_text().replace(' ', '_').replace('/', '').replace(',', '') + '.jpg'
#     # print (directory)
#     # cv2.imwrite(filename, d) 
#     # print (images[k])
#     # print (Name[k])
#     # print (Ram)
#     # print("\n")
#     ## Set up the image URL and filename
#     image_url = Image[k+4].get("src")
#     # filename = image_url.split("/")[-1]

#     # Open the url image, set stream to True, this will return the stream content.
#     r = requests.get(image_url, stream = True)

#     # Check if the image was retrieved successfully
    
#     # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
#     r.raw.decode_content = True
#     path = '/home/saikat' + filename
    
#     # Open a local file with wb ( write binary ) permission.
#     with open(path,'wb') as f:
#         # print (f)
#         # print(r.raw)
#         # exit
#         shutil.copyfileobj(r.raw,  f)

        