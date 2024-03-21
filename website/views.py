from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home Page')

def signup(request):
    return HttpResponse('Sign Up Page')

def signin(request):
    return HttpResponse('Sign In Page')

def about(request):
    return HttpResponse('About Page')