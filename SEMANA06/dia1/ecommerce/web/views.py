from django.shortcuts import render

# Create your views here.
from .models import (Categoria,Marca,
                     Producto,ProductoImagen,
                     ProductoRelacionado)
"""
VISTAS PARA EL CATALOGO DE PRODUCTOS
"""
def index(request):
    listaCategorias = Categoria.objects.all()
    listaMarcas = Marca.objects.all()
    listaProductos = Producto.objects.all()
    context = {
        'categorias':listaCategorias,
        'marcas':listaMarcas,
        'productos':listaProductos
    }
    return render(request,'index.html',context)