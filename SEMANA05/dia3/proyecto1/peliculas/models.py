from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre    

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    imagen = models.CharField(max_length=200)
    duracion = models.IntegerField()
    
    def __str__(self):
        return self.titulo