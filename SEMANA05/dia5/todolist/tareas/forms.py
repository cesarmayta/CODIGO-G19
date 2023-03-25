from django import forms

class TareaForm(forms.Form):
    descripcion = forms.CharField(label='Agregar Tarea',max_length=254)