from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto_codigo','producto_descripcion','producto_precio')
    list_editable = ('producto_precio',)
    
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cliente_ruc','cliente_rsocial','cliente_direccion','cliente_estado')
    list_editable = ('cliente_estado',)