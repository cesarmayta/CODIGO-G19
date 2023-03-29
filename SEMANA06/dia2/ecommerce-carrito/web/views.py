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

def producto(request,producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    context = {
        'producto':objProducto
    }
    return render(request,'producto.html',context)

""" CARRITO DE COMPRAS """
from .carrito import Cart

def carrito(request):
    request.session["total"] = 100
    return render(request,'carrito.html')

def agregarCarrito(request,producto_id):
    cantidad = 1
    
    objProducto = Producto.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,cantidad)
    
    #print(request.session.get("cart"))
    
    return render(request,'carrito.html')
    