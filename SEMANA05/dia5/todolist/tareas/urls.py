from django.urls import path

from . import views

app_name='tareas'

urlpatterns = [
    path('', views.index),
    path('eliminar/<int:tarea_id>',views.eliminar,name='eliminar'),
    path('completar/<int:tarea_id>',views.completar,name='completar')
]