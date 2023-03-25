from django.shortcuts import render

from .models import Tarea
from .forms import TareaForm

# Create your views here.
def index(request):
    
    if request.method == "POST":
        formNuevaTarea = TareaForm(request.POST)
        if formNuevaTarea.is_valid():
            dataTarea = formNuevaTarea.cleaned_data
            
            objTarea = Tarea(descripcion=dataTarea['descripcion'])
            objTarea.save()
    
    listaTareas = Tarea.objects.all()
    
    formTarea = TareaForm()
    
    context = {
        'tareas':listaTareas,
        'form':formTarea
    }
    return render(request,'index.html',context)