from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'homepage'),
    path('signup/', views.signup, name= 'signup-page'),
    path('signin/', views.signin, name= 'signin-page'),
    path('about/', views.about, name= 'aboutpage')
]