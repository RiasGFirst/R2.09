from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('bonjour/', views.bonjour),
    path('formulaire/', views.formulaire)
]