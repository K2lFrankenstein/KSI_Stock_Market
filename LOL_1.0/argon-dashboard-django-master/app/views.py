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

# def histo_graph(request):
#     return render(request, 'Histo.html', {})

# def line_graph(request):
#     return render(request, 'Linechart-Close.html', {})

# def RMSD_graph(request):
#     return render(request, 'RM-SD.html', {})

def search(request):
    print("In search fun")
    if request.method == "GET":
        print("inside IF")
        searched = str(request.GET['searched'])

    # q = request.GET.get('q')
        print(searched)
       
        products = Products.objects.filter( Q(name__icontains=searched) | Q(code__icontains=searched)).values()
        # # x= str(products)
        code = products[0]['code']
        company = products[0]['name']
        print("company",company)
        print("code", code)
#  calling arima function arima(code)
        arima_fun()
        graphs_fun()
#  views second function  return render(xxxxxx, 'RM - .html
        return render(request, 'icons.html', {'company': company,
                                                'code' : code})
    else:
        print("insode else")
        return render(request, 'index.html', {})


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
