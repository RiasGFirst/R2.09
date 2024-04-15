from django.urls import path
from . import views, categorie_views

urlpatterns = [
    path('', views.index),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('traitementupdate/<int:id>/', views.traitementupdate),
    path('remove/<int:id>/', views.remove),
    path('categorie/', categorie_views.index),
    path('categorie/ajout/', categorie_views.ajout),
    path('categorie/traitement/', categorie_views.traitement),
    path('categorie/affiche/<int:id>/', categorie_views.affiche),
    path('categorie/update/<int:id>/', categorie_views.update),
    path('categorie/traitementupdate/<int:id>/', categorie_views.traitementupdate),
    path('categorie/remove/<int:id>/', categorie_views.remove),
]