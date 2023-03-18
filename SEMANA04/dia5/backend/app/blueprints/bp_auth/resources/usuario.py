from flask_restful import Resource,Api
from flask import request
from .. import bp_auth

from flask_jwt_extended import create_access_token
api = Api(bp_auth)


class UsuarioResource(Resource):
    
    def get(self):
        context = {
            'status':True,
            'conent':'auth service'
        }
        
        return context

api.add_resource(UsuarioResource,'/')