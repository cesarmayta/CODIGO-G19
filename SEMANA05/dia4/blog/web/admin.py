from django.contrib import admin

# Register your models here.
from .models import (
    Autor,Articulo,Comentario
)

admin.site.register(Autor)
admin.site.register(Articulo)
admin.site.register(Comentario)