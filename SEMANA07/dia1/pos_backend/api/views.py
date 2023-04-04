from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Mesa,Categoria
)

from .serializers import (
    MesaSerializer,
    CategoriaSerializer
)

class MesaView(APIView):
    
    def get(self,request):
        data = Mesa.objects.all()
        serData = MesaSerializer(data,many=True)
        
        context = {
            'ok':True,
            'content':serData.data
        }
        
        return Response(context)