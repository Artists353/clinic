from django.urls import path
from . import views

#Путь к панели администратора 
urlpatterns = [
    path('', views.index), 
    path('about', views.about),
    path('doctors', views.doctors),
]
