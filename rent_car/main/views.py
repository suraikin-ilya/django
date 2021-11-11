from django.shortcuts import render
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer, OrderSerializer
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponse


def index(request):
    cars = Car.objects.all()
    return render(request, 'index/index.html', {'cars': cars})


def landing(request):
    return render(request, 'landing/landing.html')


class CarView(generics.CreateAPIView):
    serializer_class = CarSerializer


class OrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer


def rent(request, car_id):

    return render(request, 'index/rent.html')

