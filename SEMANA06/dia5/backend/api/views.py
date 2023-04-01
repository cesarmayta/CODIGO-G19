from rest_framework import generics

from .models import Producto
from .serializers import ProductoSerializer

class ProductoView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProductoSerializer
    lookup_url_kwarg = 'producto_id'
    queryset = Producto.objects.all()