from django.shortcuts import render,redirect,get_object_or_404

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

def eliminar(request,tarea_id):
    objTarea = get_object_or_404(Tarea,pk=tarea_id)
    objTarea.delete()
    
    return redirect('/')

def completar(request,tarea_id):
    objTarea = Tarea.objects.get(pk=tarea_id)
    objTarea.estado = 'Terminado'
    objTarea.save()
    
    return redirect('/')