from rest_framework import viewsets

from api.models import (
    Mesa,Categoria,Plato
)

from api.serializers import (
    MesaSerializer,CategoriaSerializer,
    PlatoSerializer
)

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer