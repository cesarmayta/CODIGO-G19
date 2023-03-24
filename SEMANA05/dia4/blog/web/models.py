from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nombre
    
class Articulo(models.Model):
    titulo = models.CharField(max_length=100,unique=True)
    resumen = models.TextField(help_text='Resumen')
    contenido = models.TextField()
    tiempo_registro = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo,on_delete=models.RESTRICT)
    texto = models.TextField(help_text='Tu comentario',verbose_name='Comentario')
    
    def __str__(self):
        return self.texto