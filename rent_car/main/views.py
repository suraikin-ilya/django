from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer, OrderSerializer
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .forms import *
from .models import *


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
    cars = Car.objects.all()
    return render(request, 'index/rent.html', {'cars': cars})


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'index/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'index/login.html'


def logout_user(request):
    logout(request)
    return redirect('login')


def order_car(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('')
            except:
                form.add_error(None, 'Заказ успешно отправлен')

    else:
        form = OrderForm()
    return render(request, 'index/order_car.html', {'form': form})


def news(request):
    new = News.objects.all()
    return render(request, 'index/news.html', {'news': new})


def stock(request):
    stocks = Stock.objects.all()
    return render(request, 'index/stock.html', {'stock': stocks})
