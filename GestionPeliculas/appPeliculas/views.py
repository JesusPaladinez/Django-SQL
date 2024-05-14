import os
from django.conf import settings
from django.shortcuts import render,redirect
from django.db import Error
from django.http import JsonResponse
from appPeliculas.models import Genero,Pelicula
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def inicio(request):
    return render(request,"inicio.html")

def vistaAgregarGenero(request):
    return render(request,'agregarGenero.html')

@csrf_exempt
def agregarGenero(request):
    try:
        nombre = request.POST['txtNombre']
        genero = Genero(genNombre=nombre)
        genero.save()
        mensaje = "Genero Agregado Correctamente"
    except Exception as error:
        mensaje = str(error)
    retorno = {"mensaje": mensaje}
    return render(request, 'agregarGenero.html', retorno)

def listarPeliculas(request):
    peliculas = Pelicula.objects.all()
    retorno = {"peliculas": peliculas}
    return render(request,"listarPeliculas.html",retorno)

def vistaAgregarPeliculas(request):
    generos = Genero.objects.all()
    retorno = {"generos":generos}
    return render(request,"agregarPeliculas.html",retorno)

@csrf_exempt
def agregarPeliculas(request):
    try:
        codigo = request.POST['txtCodigo']
        titulo = request.POST['txtTitulo']
        protagonista = request.POST['txtProtagonista']
        duracion = int(request.POST['txtDuracion'])
        resumen = request.POST['txtResumen']
        foto = request.FILES['fileFoto']
        idGenero = int(request.POST['cbGenero'])
        genero = Genero.objects.get(pk=idGenero)
        
        pelicula = Pelicula(
            pelCodigo = codigo,
            pelTitulo = titulo,
            pelProtagonista = protagonista,
            pelDuracion = duracion,
            pelResumen = resumen,
            pelFoto = foto,
            pelGenero = genero
        )  
            
        pelicula.save()
        mensaje = "Pelicula Agregada Correctamente"
        return redirect('/listarPeliculas/')
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje":mensaje,'idPelicula':pelicula.id}
    return render(request,"agregarPeliculas.html",retorno)

def consultarPeliculaId(request,id):
    pelicula = Pelicula.objects.get(pk=id)
    generos = Genero.objects.all()
    retorno = {"pelicula":pelicula,"generos":generos}
    return render(request,"actualizarPelicula.html",retorno)

def actualizarPelicula(request):
    try:
        idPelicula = request.POST['idPelicula']
        peliculaActulizar = Pelicula.objects.get(pk=idPelicula)
        peliculaActulizar.pelCodigo = request.POST['txtCodigo']
        peliculaActulizar.pelTitulo = request.POST['txtTitulo']
        peliculaActulizar.pelProtagonista = request.POST['txtProtagonista']
        peliculaActulizar.pelDuracion = int(request.POST['txtDuracion'])
        peliculaActulizar.pelResumen = request.POST['txtResumen']
        idGenero = int(request.POST['cbGenero'])
        genero = Genero.objects.get(pk=idGenero)
        peliculaActulizar.pelGenero = genero
        foto = request.FILES.get('fileFotos')
        if (foto):
            os.remove(os.path.join(settings.MEDIA_ROOT + "/" + str(peliculaActulizar.pelFoto)))
            peliculaActulizar.pelFoto = foto
        peliculaActulizar.save()
        mensaje = "Pelicula Actualizada"
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje":mensaje}
    return JsonResponse(retorno)

def eliminarPelicula(request,id):
    try:
        peliculaEliminar = Pelicula.objects.get(pk=id)
        peliculaEliminar.delete() 
        mensaje = "Pelicula Eliminada Correctamente"
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje":mensaje}
    return redirect('/listarPeliculas')

    