from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic.edit import CreateView


def welcome(request):
    return render(request, 'PlacesRemember/welcome.html')
def home(request):
    user = User.objects.get(pk = request.user.pk)
    places = Place.objects.all().filter(profile = user.profile)
    form = PlaceForm()
    context = {'title': 'Страница пользователя', 'places': places,'form': form, }
    return render(request, 'PlacesRemember/home.html', context)

def create(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit = False)
            user = User.objects.get(pk = request.user.pk)
            place.profile = user.profile
            place.save()
            
            return redirect('map')
        else:
             return redirect('home')
    form = PlaceForm()
    context = {'title': 'Страница добавления', 'form': form, }
    return render(request, 'PlacesRemember/create.html', context)
