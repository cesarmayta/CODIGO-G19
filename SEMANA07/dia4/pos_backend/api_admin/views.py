from rest_framework import viewsets

from api.models import (
    Mesa
)

from api.serializers import (
    MesaSerializer
)

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer