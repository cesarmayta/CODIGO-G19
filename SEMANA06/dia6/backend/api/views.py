from rest_framework import generics

from .models import (
    Producto,Cliente,FacturaCab,FacturaDet)
from .serializers import (
    ProductoSerializer,ClienteSerializer,
    FacturaSerializer,FacturaDetalleSerializer)

""" API REST PRODUCTOS """
class ProductoView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProductoSerializer
    lookup_url_kwarg = 'producto_id'
    queryset = Producto.objects.all()
    
""" API REST PARA CLIENTES """   
class ClienteView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ClienteSerializer
    lookup_url_kwarg = 'cliente_id'
    queryset = Cliente.objects.all()
    
""" API REST PARA FACTURAS """   
class FacturaView(generics.ListCreateAPIView):
    queryset = FacturaCab.objects.all()
    serializer_class = FacturaSerializer

class FacturaDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = FacturaSerializer
    lookup_url_kwarg = 'factura_id'
    queryset = FacturaCab.objects.all()
    
class FacturaDetalleView(generics.ListCreateAPIView):
    queryset = FacturaDet.objects.all()
    serializer_class = FacturaDetalleSerializer

class FacturaDetalleDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = FacturaDetalleSerializer
    lookup_url_kwarg = 'factura_detalle_id'
    queryset = FacturaDet.objects.all()