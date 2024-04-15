from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LivreForm, CategorieForm
from . import models
# Create your views here.


def index(request):
    Categorie = models.Categorie.objects.all() # récupération de tous les Livres dans la base
    return render(request,"bibliotheque/Categorie/index.html",{"Categorie": Categorie}) # envoie des données à la page index.html


def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = CategorieForm(request.POST)
        if form.is_valid(): # validation du formulaire.
            Categorie = form.save() # sauvegarde dans la base
            return render(request,"bibliotheque/Categorie/affiche.html",{"Categorie" : Categorie}) # envoie vers une page d'affichage du Livre créé
        else:
            return render(request,"bibliotheque/Categorie/ajout.html",{"form": form})
    else:
        form = CategorieForm() # création d'un formulaire vide
        return render(request,"bibliotheque/Categorie/ajout.html",{"form" : form})


def traitement(request):
    lform = CategorieForm(request.POST)
    if lform.is_valid():
        Categorie = lform.save()
        return render(request,"bibliotheque/Categorie/affiche.html",{"Categorie": Categorie, "Save": True})
    else:
        return render(request,"bibliotheque/Categorie/ajout.html",{"form": lform})


def affiche(request, id):
    Categorie = models.Categorie.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"bibliotheque/Categorie/affiche.html",{"Categorie": Categorie})


def traitementupdate(request, id):
    lform = CategorieForm(request.POST)
    if lform.is_valid():
        Categorie = lform.save(commit=False) # création d'un objet Livre avec les données du formulaire mais sans l'enregistrer dans la base.
        Categorie.id = id # modification de l'id de l'objet
        Categorie.save() # mise à jour dans la base puisque l'id du Livre existe déja.
        return HttpResponseRedirect("/bibliotheque/categorie") # plutot que d'avoir un gabarit pour nous indiquer que cela c'est bien passé, nous repartons sur une autre action qui renvoie vers la page d'index de notre site (celle avec la liste des entrées)
    else:
        return render(request, "bibliotheque/Categorie/update.html", {"form": lform, "id": id})


def update(request, id):
    Categorie = models.Categorie.objects.get(pk=id)
    lform = CategorieForm(instance=Categorie) # création d'un formulaire avec les données du Livre
    return render(request,"bibliotheque/Categorie/update.html",{"form": lform, "id": id, "nom": Categorie.nom}) # envoie du formulaire à la page de mise à jour


def remove(request, id):
    Categorie = models.Categorie.objects.get(pk=id)
    Categorie.delete()
    return HttpResponseRedirect("/bibliotheque/") # renvoie vers la page d'index de notre site après la suppression du Livre

