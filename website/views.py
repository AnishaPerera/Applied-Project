from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'website/home.html')

def services(request):
    return render(request, 'website/services.html')

def about(request):
    return render(request, 'website/about.html')

@login_required
def dashboard(request):
    return render(request, 'website/welcome.html')