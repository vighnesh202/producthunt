# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:28:13 2020

@author: vighnesh.paramasivam
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path("<int:product_id>/", views.detail, name='detail'),
]
