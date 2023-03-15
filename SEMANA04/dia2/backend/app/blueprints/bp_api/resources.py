from flask_restful import Resource,Api
from flask import request
from . import bp_api

api = Api(bp_api)

class IndexResource(Resource):
    
    def get(self):
        context = {
            'status':True,
            'content':'api rest activo'
        }
        
        return context

api.add_resource(IndexResource,'/')