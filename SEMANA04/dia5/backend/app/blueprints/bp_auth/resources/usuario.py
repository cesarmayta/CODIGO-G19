from flask_restful import Resource,Api
from flask import request
from .. import bp_auth

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

api = Api(bp_auth)


class UsuarioResource(Resource):
    
    @jwt_required()
    def get(self):
        context = {
            'status':True,
            'conent':'auth service'
        }
        
        return context
    
    def post(self):
        username = request.json.get("username",None)
        password = request.json.get("password",None)
        
        payload = {
            'usuario':username
        }
        
        if username == "admin" and password == "admin":
            access_token = create_access_token(payload)
        else:
            access_token = 'credenciales no validas'
            
        context = {
            'status':True,
            'content':access_token
        }
        
        return context

api.add_resource(UsuarioResource,'/')