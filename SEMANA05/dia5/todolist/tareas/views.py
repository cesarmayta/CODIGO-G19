from django.shortcuts import render

from .models import Tarea
# Create your views here.
def index(request):
    listaTareas = Tarea.objects.all()
    
    context = {
        'tareas':listaTareas
    }
    return render(request,'index.html',context)