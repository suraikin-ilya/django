from django.urls import path
from . import views
from .views import RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', views.index, name='index'),
    path('landing', views.landing, name='landing'),
    path('car/', views.CarView.as_view(), name='car'),
    path('order/', views.OrderView.as_view(), name='order'),
    path('rent/<int:car_id>/', views.rent, name='rent'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]
