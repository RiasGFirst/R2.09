from django.urls import path
from . import views, anime_views, studio_views

urlpatterns = [
    path('', views.home),
]