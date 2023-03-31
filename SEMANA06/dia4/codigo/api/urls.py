from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('alumno',views.getAlumno),
    path('home',views.home),
    path('setalumno',views.setAlumno),
    path('profesor',views.profesor),
    path('profesor/<int:profesor_id>',views.profesor_detail),
    path('curso',views.curso),
    path('curso/<int:curso_id>',views.curso_detail)
]