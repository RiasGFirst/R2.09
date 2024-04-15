from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class AnimeForm(ModelForm):
    class Meta:
        model = models.Anime
        fields = ['titre', 'auteur', 'date_parution', 'duree', 'resume', 'studio']
        labels = {
            'titre': _('Titre'),
            'auteur': _('Auteur'),
            'date_parution': _('Date de parution'),
            'duree': _('Durée'),
            'resume': _('Résumé'),
            'studio': _('Studio'),
        }
        help_texts = {
            'titre': _('Entrez le titre de l\'anime'),
            'auteur': _('Entrez le nom de l\'auteur'),
            'date_parution': _('Entrez la date de parution'),
            'duree': _('Entrez la durée de l\'anime'),
            'resume': _('Entrez le résumé de l\'anime'),
            'studio': _('Entrez le studio de production'),
        }
        error_messages = {
            'titre': {
                'max_length': _("Le titre est trop long."),
            },
            'auteur': {
                'max_length': _("Le nom de l'auteur est trop long."),
            },
        }


class StudioForm(ModelForm):
    class Meta:
        model = models.Studio
        fields = ['nom', 'date_creation', 'adresse']
        labels = {
            'nom': _('Nom'),
            'date_creation': _('Date de création'),
            'adresse': _('Adresse'),
        }
        help_texts = {
            'nom': _('Entrez le nom du studio'),
            'date_creation': _('Entrez la date de création'),
            'adresse': _('Entrez l\'adresse du studio'),
        }
        error_messages = {
            'nom': {
                'max_length': _("Le nom du studio est trop long."),
            },
            'adresse': {
                'max_length': _("L'adresse du studio est trop long."),
            },
        }

