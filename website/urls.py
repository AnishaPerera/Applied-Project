from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'homepage'),
    path('services/', views.services, name= 'servicespage'),
    path('about/', views.about, name= 'aboutpage'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
]