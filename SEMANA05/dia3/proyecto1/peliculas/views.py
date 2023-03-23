from django.shortcuts import render

# Create your views here.
from .models import Pelicula

def index(request):
    listaPeliculas = Pelicula.objects.all()
    
    context = {
        'peliculas':listaPeliculas
    }
    
    return render(request,'index.html',context)