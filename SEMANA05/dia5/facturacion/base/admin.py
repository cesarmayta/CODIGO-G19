from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Cliente)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto_codigo','producto_descripcion','producto_precio')
    list_editable = ('producto_precio',)