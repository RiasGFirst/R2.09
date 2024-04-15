from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = ('titre', 'auteur', 'date_parution', 'nombre_pages', 'resume', 'categorie')
        labels = {
            'titre': _('Titre'),
            'auteur': _('Auteur'),
            'date_parution': _('date de parution'),
            'nombre_pages': _('nombres de pages'),
            'resume': _('Résumé'),
            'categorie': _('Catégorie')
        }
        help_texts = {
            'titre': _('Entrez le titre du livre'),
            'auteur': _('Entrez le nom de l\'auteur'),
            'date_parution': _('Entrez la date de parution'),
            'nombre_pages': _('Entrez le nombre de pages'),
            'resume': _('Entrez un résumé du livre'),
            'categorie': _('Choisissez une catégorie')
        }


class CategorieForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ('nom', 'description')
        labels = {
            'nom': _('Nom'),
            'description': _('Description')
        }
        help_texts = {
            'nom': _('Entrez le nom de la catégorie'),
            'description': _('Entrez la description de la catégorie')
        }

