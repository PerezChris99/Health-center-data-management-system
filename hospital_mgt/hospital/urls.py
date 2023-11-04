from django.contrib import admin
from django.urls import path
from hospital.views import About, Home

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
]
