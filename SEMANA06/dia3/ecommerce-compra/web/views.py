from django.shortcuts import render,redirect

# Create your views here.
from .models import (Categoria,Marca,
                     Producto,ProductoImagen,
                     ProductoRelacionado,Cliente,
                     Pedido,PedidoDetalle)
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
    return render(request,'carrito.html')

def agregarCarrito(request,producto_id):
    if request.method == "POST":
        cantidad = int(request.POST['cantidad'])
    else:
        cantidad = 1
    
    objProducto = Producto.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,cantidad)
    
    #print(request.session.get("cart"))
    if request.method == "GET":
        return redirect("/")
    
    
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.delete(objProducto)

    return render(request,'carrito.html')

def limpiarCarrito(request):
    carritoProducto = Cart(request)
    carritoProducto.clear()
    
    return render(request,'carrito.html')
      
      
""" USUARIOS Y CLIENTES """
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

def crearUsuario(request):
    if request.method == "POST":
        dataUsuario = request.POST['nuevo_usuario']
        dataPassword = request.POST['nuevo_password']
        
        objUsuario = User.objects.create_user(username=dataUsuario,password=dataPassword)
        if objUsuario is not None:
            login(request,objUsuario)
            return redirect("/cuenta")
            
    return render(request,'login.html')

def loginUsuario(request):
    paginaDestino = request.GET.get('next',None)
    context = {
        'destino':paginaDestino
    }
    if request.method == "POST":
        dataUsuario = request.POST["usuario"]
        dataPassword = request.POST["password"]
        dataDestino = request.POST['destino']
        
        objUsuario = authenticate(request,username=dataUsuario,password=dataPassword)
        if objUsuario is not None:
            login(request,objUsuario)
            
            if dataDestino != 'None':
                return redirect(dataDestino)
            
            return redirect("/cuenta")
        else:
            context = {
                'mensajeError':'Datos Incorrectos'
            }
        
        
    return render(request,'login.html',context)

from .forms import ClienteForm

def cuentaUsuario(request):
    
    try:
        objCliente = Cliente.objects.get(usuario=request.user)
        
        dataCliente = {
            'dni':objCliente.dni,
            'nombre':request.user.first_name,
            'apellidos':request.user.last_name,
            'email': request.user.email,
            'direccion':objCliente.direccion,
            'telefono':objCliente.telefono,
            'sexo':objCliente.sexo,
            'fecha_nacimiento':objCliente.fecha_nacimiento
        }
    except:
        dataCliente = {
            'nombre':request.user.first_name,
            'apellidos':request.user.last_name,
            'email':request.user.email
        }
    
    frmCliente = ClienteForm(dataCliente)
    context = {
        'frmCliente':frmCliente
    }
    return render(request,'cuenta.html',context)

def actualizarCliente(request):
    mensaje = ""
    frmCliente = ClienteForm(request.POST)
    if frmCliente.is_valid():
        dataCliente = frmCliente.cleaned_data
            
        #actualizar usuario
        actUsuario = User.objects.get(pk=request.user.id)
        actUsuario.first_name = dataCliente["nombre"]
        actUsuario.last_name = dataCliente["apellidos"]
        actUsuario.email = dataCliente["email"]
        actUsuario.save()
            
        #registrar Cliente
        try:
            objCliente = Cliente.objects.get(usuario=request.user)
        except:
            objCliente = Cliente()
                
        objCliente.usuario = actUsuario
        objCliente.nombre = dataCliente["nombre"] + " " + dataCliente["apellidos"]
        objCliente.dni = dataCliente["dni"]
        objCliente.direccion = dataCliente["direccion"]
        objCliente.telefono = dataCliente["telefono"]
        objCliente.sexo = dataCliente["sexo"]
        objCliente.fecha_nacimiento = dataCliente["fecha_nacimiento"]
        objCliente.save()
            
        mensaje = "Datos Actualizados"
            
    context = {
        'mensaje':mensaje,
        'frmCliente':frmCliente
    }
                
    return render(request,'cuenta.html',context)

""" VISTAS PARA PEDIDOS """
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def registrarPedido(request):
    context = {
        
    }
    return render(request,'pedido.html',context)