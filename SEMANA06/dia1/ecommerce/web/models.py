from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'tbl_categoria'
        
    def __str__(self):
        return self.nombre
    
class Marca(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'tbl_marca'
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    marca= models.ForeignKey(Marca,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=254)
    descripcion = models.TextField(null=True)
    detalle = models.TextField(null=True)
    caracteristicas = models.TextField(null=True)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    imagen = models.ImageField(upload_to='productos',blank=True)
    
    class Meta:
        db_table = 'tbl_producto'
    
    def __str__(self):
        return self.nombre
    
class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.RESTRICT)
    imagen = models.ImageField(upload_to='galeria',blank=True)
    
    class Meta:
        db_table = 'tbl_producto_imagen'
        
    def __str__(self):
        return self.producto.nombre
    
class ProductoRelacionado(models.Model):
    producto = models.ForeignKey(Producto,related_name='Principal',on_delete=models.RESTRICT)
    relacionado = models.ForeignKey(Producto,related_name='Relacionado',on_delete=models.RESTRICT)
    
    class Meta:
        db_table = 'tbl_producto_relacionado'
        
    def __str__(self):
        return self.relacionado.nombre
        
    
    
