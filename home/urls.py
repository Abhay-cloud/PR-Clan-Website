from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('apply', views.application, name='application'),
    path('happynewyear', views.newyear, name='newyear'),
    path('a6H3qn9j', views.nitro, name='newyear'),
]