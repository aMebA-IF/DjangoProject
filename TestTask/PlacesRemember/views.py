from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import *
from .models import *
from decimal import Decimal
from django.views.generic.edit import CreateView


def welcome(request):
    context = {'title': 'Добро пожаловать'}
    return render(request, 'PlacesRemember/welcome.html', context)

def home(request):
    user = User.objects.get(pk = request.user.pk)
    places = Place.objects.all().filter(profile = user.profile)
    context = {'title': 'Страница пользователя', 'places': places }
    return render(request, 'PlacesRemember/home.html', context)


def create(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit = False)
            user = User.objects.get(pk = request.user.pk)
            place.profile = user.profile
            place.save()
            return redirect('home')
        else:
             return redirect('welcome')
    form = PlaceForm()
    context = {'title': 'Страница добавления', 'form': form, }
    return render(request, 'PlacesRemember/create.html', context)

    
def details(request, pk):

        сPlace = Place.objects.get(id = pk)
        context = {
                'place': сPlace,
                'title': 'Детализация места',
                }        
        return render(request, "PlacesRemember\details.html", context)

def edit(request, pk):

        сPlace = Place.objects.get(id = pk)
        context = {
                'place': сPlace,
                'title': 'Изменение места',
                }
        if request.method == "POST":
            сPlace.name = request.POST.get("name")
            сPlace.comment = request.POST.get("comment")
            сPlace.latitude = Decimal(str(request.POST.get("latitude")).replace(',','.'))
            сPlace.longitude = Decimal(str(request.POST.get("longitude")).replace(',','.'))
            сPlace.save()
            return redirect("home")
            
        return render(request, "PlacesRemember\edit.html", context)