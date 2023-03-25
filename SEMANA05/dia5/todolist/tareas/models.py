from django.db import models

# Create your models here.
class Tarea(models.Model):
    descripcion = models.CharField(max_length=254)
    fecha_registro = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=100,default='pendiente')
    
    def __str__(self):
        return self.descripcion