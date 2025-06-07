from django.urls import path
from . import views

#Путь к панели администратора 
urlpatterns = [
    path('', views.index, name='index'), 
    path('about', views.about, name='about'),
    path('doctors', views.doctors, name='doctors'),
]
