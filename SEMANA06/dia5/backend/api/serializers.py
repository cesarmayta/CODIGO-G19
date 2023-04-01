from rest_framework import serializers

from .models import(
    Producto,Cliente,FacturaCab,FacturaDet
)

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaCab
        fields = '__all__'
        
class FacturaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaDet
        fields = '__all__'