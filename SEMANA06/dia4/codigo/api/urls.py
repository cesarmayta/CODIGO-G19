from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('alumno',views.getAlumno),
    path('home',views.home),
    path('setalumno',views.setAlumno),
    path('profesor',views.profesor)
]