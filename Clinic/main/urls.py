from django.urls import path
from . import views

#Путь к панели администратора 
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name="home")
]
