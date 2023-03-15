from flask_restful import Resource,Api
from flask import request
from . import bp_api

from .models import Categoria
from .schemas import CategoriaSchema

api = Api(bp_api)

class IndexResource(Resource):
    
    def get(self):
        context = {
            'status':True,
            'content':'api rest activo'
        }
        
        return context
    
    def post(self):
        pass
    
    def put(self):
        pass
        
    def delete(self):
        pass

class CategoriaResource(Resource):
    
    def get(self):
        data = Categoria.get_all()
        data_schema = CategoriaSchema(many=True)
        
        context = {
            'status':True,
            'content':data_schema.dump(data)
        }
        
        return context


api.add_resource(IndexResource,'/')
api.add_resource(CategoriaResource,'/categoria')