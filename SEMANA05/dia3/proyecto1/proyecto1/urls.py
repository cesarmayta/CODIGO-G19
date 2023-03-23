"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

def saludo(request):
    nombre = request.GET['nombre']
    return HttpResponse('<h1><center> HOLA MUNDO '+ nombre +' </center></h1')

def index(request):
    return HttpResponse('<h1>BIENVENIDO A MI PROYECTO CON DJANGO</h1>')

def suma(request,n1,n2):
    resultado = n1 + n2
    return HttpResponse('<h1>La suma de ' + str(n1) + ' + ' + str(n2) + ' es ' + str(resultado))

def calculadora(request,n1,n2,ope):
    if(ope == "suma"):
        resultado = n1 + n2
    elif(ope == "resta"):
        resultado = n1 - n2
    else:
        resultado = 0
        
    return HttpResponse('<h1>Resultado es ' + str(resultado) + '</h1>')

urlpatterns = [
    path('',index),
    path('saludo',saludo),
    path('suma/<int:n1>/<int:n2>',suma),
    path('calculadora/<int:n1>/<int:n2>/<str:ope>',calculadora),
    path('peliculas/',include('peliculas.urls')),
    path('admin/', admin.site.urls),
]
