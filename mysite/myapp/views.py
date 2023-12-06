from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    estudiantes = [ 'Alexia Asuncion', 
                    'Axel Barzola',
                    'Gerson Sahuma',
                    'Carlos tu Dios']
    return render(request,'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto Web Con DJango',
        'estudiantes': estudiantes
    })

def ventana1(request):
    return render(request,'ventana1.html',{
        'titulo':'Saludo',
        'autor_saludo':'PhD. Brian Inca'
    })


def ventana2(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request,'ventana2.html',{
        'titulo':'Rango',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
    })


def ventana3(request):
    return render(request, 'ventana3.html')
