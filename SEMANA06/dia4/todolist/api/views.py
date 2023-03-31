from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from .models import Tarea
from .serializers import TareaSerializer

class TareaView(APIView):
    
    def get(self,request):
        data = Tarea.objects.all()
        serData = TareaSerializer(data,many=True)
        return Response(serData.data)
    
    def post(self,request):
        serData = TareaSerializer(data=request.data)
        serData.is_valid(raise_exception=True)
        serData.save()
        
        return Response(serData.data)
    
class TareaDetailView(APIView):
    
    def get_object(self, pk):
        try:
            return Tarea.objects.get(pk=pk)
        except Tarea.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        data = self.get_object(pk)
        serData = TareaSerializer(data)
        return Response(serData.data)
    
    def put(self,request,pk):
        data = self.get_object(pk)
        serData = TareaSerializer(data,data=request.data)
        if serData.is_valid():
            serData.save()
            return Response(serData.data)
        return Response(serData.errors,status=status.HTTP_400_BAD_REQUEST)
    
    