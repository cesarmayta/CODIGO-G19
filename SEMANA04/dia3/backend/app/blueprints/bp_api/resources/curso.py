from flask_restful import Resource,Api
from flask import request
from .. import bp_api

from ..models import Curso
from ..schemas import CursoSchema

api = Api(bp_api)

class CursoResource(Resource):
    
    def get(self):
        data = Curso.get_all()
        data_schema = CursoSchema(many=True)
        
        context = {
            'status':True,
            'content':data_schema.dump(data)
        }
        
        return context
    
    
    def post(self):
        data = request.get_json()
        titulo = data['titulo']
        desripcion = data['descripcion']
        nivelId = data['nivel_id']
        categoriaId = data['categoria_id']
        autorId = data['autor_id']
        
        objCurso = Curso(titulo,desripcion,categoriaId,nivelId,autorId)
        objCurso.save()
        
        data_schema = CursoSchema()
        
        context = {
            'status':True,
            'content':data_schema.dump(objCurso)
        }
        
        return context
    
    
    
class CursoIdResource(Resource):
    
    def get(self,id):
        
        data = Curso.get_by_id(id)
        data_schema = CursoSchema()
        
        context = {
            'status':True,
            'content':data_schema.dump(data)
        }
        
        return context
    
    
api.add_resource(CursoResource,'/curso')
#api.add_resource(AutorResource,'/autor/<id>',endpoint='autor')
api.add_resource(CursoIdResource,'/cursoid/<id>',endpoint='cursoid')
        
