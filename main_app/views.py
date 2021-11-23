from django.shortcuts import render
from .models import Place

# Define the home view


def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


def places_index(request):
  places = Place.objects.all()
  return render(request, 'places/index.html', {'places': places})


def places_detail(request, place_id):
  place = Place.objects.get(id=place_id)
  return render(request, 'places/detail.html', { 'place': place })