from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'website/home.html')

def services(request):
    return render(request, 'website/services.html')

def about(request):
    return render(request, 'website/about.html')