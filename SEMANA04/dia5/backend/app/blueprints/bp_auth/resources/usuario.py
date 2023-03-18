from flask_restful import Resource,Api
from flask import request
from .. import bp_auth

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

from ..models import Usuario
from ..schemas import UsuarioSchema

from werkzeug.security import generate_password_hash, check_password_hash

api = Api(bp_auth)

class UsuarioResource(Resource):
    
    @jwt_required()
    def get(self):
        
        data = Usuario.get_all()
        
        data_schema = UsuarioSchema(many=True)
        
        context = {
            'status':True,
            'conent': data_schema.dump(data)
        }
        
        return context
    
    def post(self):
        username = request.json.get("username",None)
        password = request.json.get("password",None)
        
        objUsuario = Usuario(username,generate_password_hash(password))
        objUsuario.save()
        
        data_schema = UsuarioSchema()
            
        context = {
            'status':True,
            'content':data_schema.dump(objUsuario)
        }
        
        return context
    
    @jwt_required()
    def put(self,id):
        data = request.get_json()
        objUsuario = Usuario.get_by_id(id)
        objUsuario.usuario_nombre = data['username']
        objUsuario.usuario_password = generate_password_hash(data['password'])
        objUsuario.save()
        
        data_schema = UsuarioSchema()
        context = {
            'status':True,
            'content':data_schema.dump(objUsuario)
        }
        
        return context
    
    @jwt_required()
    def delete(self,id):
        objUsuario = Usuario.get_by_id(id)
        objUsuario.delete()
        
        data_schema = UsuarioSchema()
        context = {
            'status':True,
            'content':data_schema.dump(objUsuario)
        }
        
        return context
    
class UsuarioIdResource(Resource):
    @jwt_required()
    def get(self,id):
        
        data = Usuario.get_by_id(id)
        data_schema = UsuarioSchema()
        
        context = {
            'status':True,
            'content':data_schema.dump(data)
        }

        return context
    
class LoginResource(Resource):    
    def post(self):
        username = request.json.get("username",None)
        password = request.json.get("password",None)
        
        payload = {
            'username':username
        }
        
        objUsuario = Usuario.query.filter_by(usuario_nombre=username)
        #print(objUsuario)
        #print(objUsuario[0].usuario_id)

        if check_password_hash(objUsuario[0].usuario_password, password):
            payload = {
                'id':objUsuario[0].usuario_id,
                'username':username
            }
            access_token = create_access_token(payload)
        else:
            access_token = 'credenciales no validas'
            
        context = {
            'status':True,
            'content':access_token
        }
        
        return context

api.add_resource(UsuarioResource,'/usuario')
api.add_resource(UsuarioResource,'/usuario/<id>',endpoint='usuario')
api.add_resource(UsuarioIdResource,'/usuarioid/<id>',endpoint='usuarioid')
api.add_resource(LoginResource,'/login')