# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    cliente_rsocial = models.CharField(max_length=255)
    cliente_ruc = models.CharField(max_length=20)
    cliente_direccion = models.TextField()
    cliente_estado = models.CharField(max_length=1)
    cliente_fecha_log = models.DateTimeField()
    cliente_usuario_log = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_cliente'
    
    def __str__(self):
        return self.cliente_rsocial


class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    producto_codigo = models.CharField(max_length=255,verbose_name='CODIGO')
    producto_descripcion = models.CharField(max_length=255,verbose_name='PRODUCTO')
    producto_precio = models.FloatField(verbose_name='PRECIO')
    producto_estado = models.CharField(max_length=1)
    producto_fecha_log = models.DateTimeField()
    producto_usuario_log = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_producto'
        
    def __str__(self):
        return self.producto_descripcion

class FacturaCab(models.Model):
    factura_cab_id = models.AutoField(primary_key=True)
    factura_cab_serie = models.CharField(max_length=20)
    factura_cab_nro = models.CharField(max_length=255)
    factura_cab_fvencimiento = models.DateField()
    factura_cab_femision = models.DateField()
    factura_cab_tipo_moneda = models.CharField(max_length=45)
    factura_cab_observacion = models.TextField(blank=True, null=True)
    factura_cab_valorventa = models.FloatField()
    factura_cab_valorigv = models.FloatField()
    factura_cab_valortotal = models.FloatField()
    factura_cab_estado = models.CharField(max_length=1)
    factura_cab_fecha_log = models.DateTimeField()
    factura_cab_usuario_log = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_factura_cab'
        
    def __str__(self):
        return self.factura_cab_serie + '-' + self.factura_cab_nro


class FacturaDet(models.Model):
    factura_det_id = models.AutoField(primary_key=True)
    factura_det_precio = models.FloatField()
    factura_det_cantidad = models.FloatField()
    factura_det_subtotal = models.FloatField()
    factura_det_fecha_log = models.DateTimeField()
    factura_det_usuario_log = models.CharField(max_length=255)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    factura_cab = models.ForeignKey(FacturaCab, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_factura_det'
        
    def __str__(self):
        return self.factura_det_id


