from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth.models import User

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['usu_nom'] = user.first_name  + ' ' + user.last_name
        token['usu_id'] = user.id
        if user.is_superuser:
            token['usu_tipo'] = 'admin'
        else:
            token['usu_tipo'] = 'mozo'
        # ...

        return token