from django.shortcuts import render


# Create your views here.

def About(request):
    return render(request, 'about.html')

def Home(request):
    return render(request, 'home.html')
