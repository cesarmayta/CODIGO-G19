from django.shortcuts import render

# Create your views here.
from .models import Pelicula,Genero

def index(request):
    listaPeliculas = Pelicula.objects.all()
    listaGeneros = Genero.objects.all()
    
    context = {
        'peliculas':listaPeliculas,
        'generos':listaGeneros
    }
    
    return render(request,'index.html',context)

def peliculas_por_genero(request,genero_id):
    objGenero = Genero.objects.get(pk=genero_id)
    listaPeliculas = objGenero.pelicula_set.all() 
    listaGeneros = Genero.objects.all()
    
    context = {
        'peliculas':listaPeliculas,
        'generos':listaGeneros
    }
    
    return render(request,'index.html',context)
    