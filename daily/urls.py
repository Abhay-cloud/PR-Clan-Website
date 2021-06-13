
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dailyHome, name='dailyHome'),
    path('<str:slug>', views.dailyResults, name='dailyResults')
]
