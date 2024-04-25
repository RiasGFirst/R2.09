from django.shortcuts import render
from .forms import AnimeForm
# Create your views here.


def home(request):
    return render(request, 'animeapp/anime/home.html')


def add_anime(request):
    form = AnimeForm()
    return render(request, 'animeapp/anime/add.html', {'form': form})


def processing(request):
    lform = AnimeForm(request.POST)
    if lform.is_valid():
        lform.save()
        return render(request, 'animeapp/anime/success.html', {'Anime': lform.cleaned_data})
    else:
        return render(request, 'animeapp/anime/error.html')