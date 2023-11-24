from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def ventana1(request):
    return render(request, 'ventana1.html')


def ventana2(request):
    return render(request, 'ventana2.html')


def ventana3(request):
    return render(request, 'ventana3.html')
