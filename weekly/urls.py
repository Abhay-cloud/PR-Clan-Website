
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.weeklyHome, name='weeklyHome'),
    path('<str:slug>', views.weeklyResults, name='weeklyResults')
]
