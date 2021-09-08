import os
from django.db.models import Q
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
import django 
django.setup()  
from app.models import Products
import pandas as pd


def getcode(asd):

    """
    GET request will render the products that are matched with the 'q' form parameter.
    will return PRODUCT list in descending order of the stock.
    """
   
    q = asd
    print(q)
    products = Products.objects.filter( Q(name__icontains=q) | Q(code__icontains=q)).values()
 
    
    print(products[0]['code'])
    code = products[0]['code']
    company = products[0]['name']
    return code



if __name__ == '__main__' :
    print("Populating the data please wait")
    getcode(input("enter comapny name:  "))
    print(" not populating completed")    