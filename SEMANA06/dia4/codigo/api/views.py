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

@api_view(['POST'])
def setAlumno(request):
    serAlumno = AlumnoSerializer(data=request.data)
    serAlumno.is_valid(raise_exception=True)
    
    nuevoAlumno = serAlumno.save()
    
    context ={
        'status':True,
        'content':AlumnoSerializer(nuevoAlumno).data
    }
    
    return Response(context)

""" ENDPOINTS PARA PROFESOR """

from .models import Profesor
from .serializers import ProfesorSerializer

@api_view(['GET','POST'])
def profesor(request):
    if request.method == 'GET':
        data = Profesor.objects.all()
        serializer = ProfesorSerializer(data,many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serData = ProfesorSerializer(data=request.data)
        if serData.is_valid():
            serData.save()
            return Response(serData.data)
        else:
            return Response(serData.errors,status=status.HTTP_400_BAD_REQUEST)
        
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET','PUT','DELETE'])
def profesor_detail(request,profesor_id):
    try:
        objProfesor = Profesor.objects.get(pk=profesor_id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serData = ProfesorSerializer(objProfesor)
        return Response(serData.data)
    
    elif request.method == 'PUT':
        serData = ProfesorSerializer(objProfesor,data=request.data)
        if serData.is_valid():
            serData.save()
            return Response(serData.data)
        else:
            return Response(serData.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        objProfesor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
""" ENDPOINTS PARA CURSO """

from .models import Curso
from .serializers import CursoSerializer

@api_view(['GET','POST'])
def curso(request):
    if request.method == 'GET':
        data = Curso.objects.all()
        serializer = CursoSerializer(data,many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serData = CursoSerializer(data=request.data)
        if serData.is_valid():
            serData.save()
            return Response(serData.data)
        else:
            return Response(serData.errors,status=status.HTTP_400_BAD_REQUEST)
        
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET','PUT','DELETE'])
def curso_detail(request,curso_id):
    try:
        objCurso = Curso.objects.get(pk=curso_id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serData = CursoSerializer(objCurso)
        return Response(serData.data)
    
    elif request.method == 'PUT':
        serData = CursoSerializer(objCurso,data=request.data)
        if serData.is_valid():
            serData.save()
            return Response(serData.data)
        else:
            return Response(serData.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        objCurso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
