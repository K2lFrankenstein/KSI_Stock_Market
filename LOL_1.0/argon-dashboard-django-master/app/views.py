# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.db.models import Q
from django.views.generic import View, TemplateView, ListView, DetailView
from app.models import Products
import pandas as pd
from arima import arima_fun,graphs_fun
import time

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

class war:
    def setdata(company,code):
        company = company
        code = code
    def get_data():
        x= [company,code]  
        return x
G1 = war()

def search(request):
    print("In search fun")
    if request.method == "GET":
        print("inside IF")
        searched = str(request.GET['searched'])
        products = Products.objects.filter( Q(name__icontains=searched) | Q(code__icontains=searched)).values()
        code = str(products[0]['code'])
        company = str(products[0]['name'])
        print("company",company)
        print("code", code)
    else:
        print("shit happens")
    G1.setdata(company,code)
#  calling arima function arima(code)
    # arima_fun()
    # graphs_fun()
#  views second function  return render(xxxxxx, 'RM - .html
    return render(request, 'includes/sidenav.html', {'company': xyz[0],
                                                'code' : xyz[1]})



def histo_graph(request):
    xyz = globe_1(request)
    return render(request, '2.html', {'company': xyz[0],
                                            'code' : xyz[1]})

def line_graph(request):
    xyz = globe_1(request)
    return render(request, '1.html', {'company': xyz[0],
                                                'code' : xyz[1]})

def RMSD_graph(request):
    
    sigma = G1.get_data()
    print("inside rsdm")
    print(sigma[0])
    return render(request, '3.html',{'company': sigma[0],
                                          'code' : sigma[1]})       

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.

    #  qset = getcode()
    # print("qset", qset)
    # return qset

    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
