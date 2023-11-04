from django.contrib import admin
from django.urls import path
from hospital.views import About, Home, Contact

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
]
