from django.shortcuts import render

# Мы вызываем здесь метод от urls
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def doctors(request):
    return render(request, 'main/doctors.html')