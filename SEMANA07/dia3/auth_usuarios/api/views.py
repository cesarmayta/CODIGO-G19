from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import (
    TokenAuthentication,SessionAuthentication,
    BasicAuthentication)
from rest_framework.permissions import IsAuthenticated

class IndexView(APIView):
    
    def get(self,request):
        context = {
            'status':True,
            'content':'servidor activo'
        }
        return Response(context)
    
class UsuarioView(APIView):
    authentication_classes  = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        context = {
            'user':str(request.user)
        }
        return Response(context)
    
class TokenView(APIView):
    authentication_classes  = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        context = {
            'user':str(request.user)
        }
        return Response(context)
    
from rest_framework_simplejwt.authentication import JWTAuthentication
    
class JWTView(APIView):
    authentication_classes  = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        context = {
            'user':str(request.user)
        }
        return Response(context)
    
"""" TOKEN AUTHENTICATION """

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
    
class LoginTokenView(APIView):
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username,password=password)
        
        if user:
            Token.objects.get_or_create(user=user)
            context = {
                'status':True,
                'token':user.auth_token.key
            }
        else:
            context = {
                'status':False,
                'error':'datos incorrectos'
            }
            
        return Response(context)
    
""" jwt token authentication """
from rest_framework_simplejwt.tokens import RefreshToken
class LoginJWTView(APIView):
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username,password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            context = {
                'status':True,
                'token':str(refresh.access_token)
            }
        else:
            context = {
                'status':False,
                'error':'datos incorrectos'
            }
            
        return Response(context)