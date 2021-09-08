# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from app.views import search

app_name = 'app'

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('histo/', views.histo_graph, name='histo'),
    path('line/', views.line_graph, name='line'),
    path('RMSD/', views.RMSD_graph, name='RMSD'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
