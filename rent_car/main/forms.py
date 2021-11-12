from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.shortcuts import redirect

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-label'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-label'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-label'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-label'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].empty_label = "Не выбрана марка авто"

    class Meta:
        model = Order
        fields = ['car', 'user_name', 'user_phone', 'comment']


