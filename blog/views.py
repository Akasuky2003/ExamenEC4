from django.shortcuts import render
from .models import *

from .models import Services


# Create your views here.
def index(request):
    servicio=Services.objects.all()
    return render(request, 'index.html',{'servicio':servicio})
def blog(request):
    return render(request, 'blog.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')


