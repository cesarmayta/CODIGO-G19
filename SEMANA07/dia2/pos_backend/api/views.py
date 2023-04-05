from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Mesa,Categoria,Plato
)

from .serializers import (
    MesaSerializer,
    CategoriaSerializer,
    PlatoSerializer,
    CategoriaPlatosSerializer
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
    
class CategoriaView(APIView):
    
    def get(self,request):
        data = Categoria.objects.all()
        serData = CategoriaSerializer(data,many=True)
        
        context = {
            'ok':True,
            'content':serData.data
        }
        
        return Response(context)
    
class PlatoView(APIView):
    
    def get(self,request):
        data = Plato.objects.all()
        serData = PlatoSerializer(data,many=True)
        
        context = {
            'ok':True,
            'content':serData.data
        }
        
        return Response(context)
    

class CategoriaPlatosView(APIView):
    
    def get(self,request,categoria_id):
        data = Categoria.objects.get(pk=categoria_id)
        serData = CategoriaPlatosSerializer(data)
        
        context = {
            'ok':True,
            'content':serData.data
        }
        
        return Response(context)