from django.shortcuts import render
from .forms import StudioForm
# Create your views here.


def home(request):
    return render(request, 'animeapp/studio/home.html')


def add_studio(request):
    form = StudioForm()
    return render(request, 'animeapp/studio/add.html', {'form': form})


def processing(request):
    lform = StudioForm(request.POST)
    if lform.is_valid():
        Studio = lform.save()
        return render(request, 'animeapp/studio/success.html', {'Studio': Studio})
    else:
        return render(request, 'animeapp/studio/add.html', {'form': lform})

