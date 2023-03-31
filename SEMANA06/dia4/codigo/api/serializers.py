from rest_framework import serializers

from .models import Alumno,Profesor,Curso

class AlumnoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    email = serializers.EmailField()
    
    def create(self,validated_data):
        return Alumno.objects.create(**validated_data)
    
class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'