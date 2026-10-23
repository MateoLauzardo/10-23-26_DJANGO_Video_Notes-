from django.contrib import admin
from django.urls import path, include

from . import views 

urlpatterns = [
    path('greet/', views.greet),
    path('greet/<str:name>/', views.greet),
    
]