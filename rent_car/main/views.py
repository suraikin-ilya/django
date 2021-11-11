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
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')