import os
from django.db.models import Q
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
import django 
django.setup()  
from app.models import Products
import pandas as pd


def getcode(self):


    """
    GET request will render the products that are matched with the 'q' form parameter.
    will return PRODUCT list in descending order of the stock.
    """
   
    q = request.GET.get('q')
    print(q)
    products = Products.objects.filter( Q(name__icontains=q) | Q(code__icontains=q)).values()
 
    
    # # x= str(products)
    print(products[0]['code'])
    code = products[0]['code']
    return code


    # company = products.strip("<QuerySet[< >]>")

    # # company = x.strip("Products:")
    # print("comany = ",company)
    # fuck = company.split("*")
    # print(fuck)
    # # pc= Products.objects.get()
    # # print(pc)

if __name__ == '__main__' :
    print("Populating the data please wait")
    getcode(input("enter comapny name:  "))
    print(" not populating completed")    