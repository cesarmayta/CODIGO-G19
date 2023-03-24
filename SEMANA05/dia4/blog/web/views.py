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

def articulo(request,articulo_id):
    objArticulo = Articulo.objects.get(pk=articulo_id)
    
    context= {
        'articulo':objArticulo
    }
    
    return render(request,'articulo.html',context)