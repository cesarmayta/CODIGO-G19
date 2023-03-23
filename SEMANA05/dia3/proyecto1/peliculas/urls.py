from django.urls import path

from . import views

app_name = 'peliculas'

urlpatterns = [
    path('',views.index),
    path('<int:genero_id>',views.peliculas_por_genero,name='genero')
]