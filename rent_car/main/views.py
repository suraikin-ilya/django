from django.shortcuts import render
from .models import Car, Photo
# from django.http import HttpResponse


def index(request):
    cars = Car.objects.all()
    photos = Photo.objects.all()
    return render(request, 'index/index.html', {'cars': cars, 'photos': photos})

def landing(request):
    return render(request, 'landing/landing.html')

