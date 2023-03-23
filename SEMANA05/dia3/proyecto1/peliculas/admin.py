from django.contrib import admin

# Register your models here.
from .models import Pelicula,Genero

admin.site.register(Pelicula)
admin.site.register(Genero)