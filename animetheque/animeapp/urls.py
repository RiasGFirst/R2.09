from django.urls import path
from . import views, anime_views, studio_views

urlpatterns = [
    path('', views.home),
    path('anime/', anime_views.home),
    path('anime/add/', anime_views.add_anime),
    path('anime/processing/', anime_views.processing),
    path('studio/', studio_views.home),
    path('studio/add/', studio_views.add_studio),
    path('studio/processing/', studio_views.processing),
]