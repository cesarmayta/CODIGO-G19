from django.shortcuts import render

from .models import (
    Autor,Articulo,Comentario
)

# Create your views here.
def index(request):
    listaArticulos = Articulo.objects.all()
    
    context = {
        'articulos':listaArticulos
    }
    
    return render(request,'index.html',context)