from rest_framework import serializers

from .models import(
    Producto,Cliente,FacturaCab,FacturaDet
)

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'