# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = 'authentication'
urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/login.html',next_page=None),name = "logout"),
    # path('logout/', LogoutView.as_view(), name="logout")
]
