from django.shortcuts import render, redirect
from .models import Clinic
from .forms import ClinicForm

# Мы вызываем здесь метод от urls
def index(request):
    clinic = Clinic.objects.all()
    
    if request.method == "POST":
        form = ClinicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # 'home' замените на имя вашего URL
    else:
        form = ClinicForm()

    return render(request, 'main/index.html', {'clinic': clinic, 'form': form})

def home(request):
    return render(request, 'main/home.html')