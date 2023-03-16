from flask_restful import Resource,Api
from flask import request
from .. import bp_api

from ..models import Autor
from ..schemas import AutorSchema

api = Api(bp_api)

class AutorResource(Resource):
    
    def get(self):
        pass
    
    def post(self):
        data = request.get_json()
        nombre = data['nombre']
        foto = data['foto']
        descripcion = data['descripcion']
        objAutor = Autor(nombre,foto,descripcion)
        objAutor.save()
        
        data_schema = AutorSchema()
        
        context = {
            'status':True,
            'content':data_schema.dump(objAutor)
        }
        
        return context
    
    
api.add_resource(AutorResource,'/autor')
        
