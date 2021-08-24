# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=400)
    code = models.CharField(max_length=300)

    def __str__(self):
        # x = (self.name+"*"+self.code)
        return self.name
  
# ### search 
# # class SearchView(View):
#     """
#     This View handles one HTTP methods. GET.
#     GET request will render the products that are matched with the 'q' form parameter.
#     """
    
# def some(self):
#     """
#     GET request will render the products that are matched with the 'q' form parameter.
#     will return PRODUCT list in descending order of the stock.
#     """
#     q ="Shree Ajit Pulp"     #request.GET.get('q')
#     products = models.Products.objects.filter(is_deleted=False).filter(
#         Q(name_icontains=q) | Q(code_icontains=q)
#     ).order_by()

#     return render(request, 'my_app/search.html', context={'products': products})

