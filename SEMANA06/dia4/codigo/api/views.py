from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import Alumno

# Create your views here.
def index(request):
    context = {
        'status':True,
        'content':'Bienvenido a mi API con Django'
    }
    
    return JsonResponse(context)

@api_view(['GET'])
def home(request):
    context = {
        'status':True,
        'content':'Bienvenido a mi API con DRF'
    }
    
    return Response(context)

def alumno(request):
    dataAlumnos = Alumno.objects.all()
    #serialización
    listaAlumnos = []
    for alumno in dataAlumnos:
        dicAlumno = {
            'nombre':alumno.nombre,
            'email':alumno.email
        }
        listaAlumnos.append(dicAlumno)
    
    context = {
        'status':True,
        'content':listaAlumnos
    }
    
    return JsonResponse(context)

from .serializers import AlumnoSerializer

@api_view(['GET'])
def getAlumno(request):
    dataAlumnos = Alumno.objects.all()
    serAlumnos = AlumnoSerializer(dataAlumnos,many=True)
    
    context = {
        'status':True,
        'content':serAlumnos.data
    }
    
    return Response(context)
    
