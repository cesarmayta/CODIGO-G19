from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class IndexView(APIView):
    
    def get(self,request):
        context = {
            'status':True,
            'content':'servidor activo'
        }
        return Response(context)
    
class UsuarioView(APIView):
    authentication_classes  = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        context = {
            'user':str(request.user)
        }
        return Response(context)
    
