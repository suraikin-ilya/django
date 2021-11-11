from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('landing', views.landing, name='landing'),
    path('car/', views.CarView.as_view(), name='car'),
    path('order/', views.OrderView.as_view(), name='order'),
    path('rent/<int:car_id>/', views.rent, name='rent')

]
