from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import Articulo

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


def crear_articulo(request,titulo, contenido, publicado):
    articulo = Articulo(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")

def buscar_articulo(request):
    try:
        articulo = Articulo.objects.get(id=1000)
        resultado = f"""Articulo: 
                        <br> <strong>ID:</strong> {articulo.id} 
                        <br> <strong>Título:</strong> {articulo.titulo} 
                        <br> <strong>Contenido:</strong> {articulo.contenido}
                        """
    except:
        resultado = "<h1> Artículo No Encontrado </h1>"
    return HttpResponse(resultado)


def editar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)

    articulo.titulo = "Enseñanza presencial en la UNTELS"
    articulo.contenido = "Aula Virtual, Google Meet, Portal Académico, Google Classroom..."
    articulo.publicado = False

    articulo.save()
    return HttpResponse(f"Articulo Editado: {articulo.titulo} - {articulo.contenido}")


def listar_articulos(request):
    articulos = Articulo.objects.filter(titulo="ansiedad de los devs")
    return render(request, 'listar_articulos.html',{
        'articulos':articulos,
        'titulo': 'Listado de Artículos'
    })


def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()
    return redirect('listar_articulos')