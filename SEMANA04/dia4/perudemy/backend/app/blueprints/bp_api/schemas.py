#create your schemas
from utils.db import ma
from marshmallow import fields

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('categoria_id','categoria_descripcion')
        
class NivelSchema(ma.Schema):
    class Meta:
        fields = ('nivel_id','nivel_descripcion')
        
class AutorSchema(ma.Schema):
    class Meta:
        fields = ('autor_id','autor_nombre','autor_foto','autor_descripcion')
               
class CursoSchema(ma.Schema):
    id = fields.Integer(attribute="curso_id")
    category = fields.String(attribute="cat.categoria_descripcion")
    title = fields.String(attribute="curso_titulo")
    description = fields.String(attribute="curso_descripcion")
    level = fields.String(attribute="niv.nivel_descripcion")
    teacher = fields.String(attribute="aut.autor_nombre")
    duration = fields.Integer(attribute="curso_duracion")
    lectures = fields.Integer(attribute="curso_clases")
    stars = fields.Integer(attribute="curso_calificacion")
    price = fields.Integer(attribute="curso_precio")
    img = fields.String(attribute="curso_imagen")
    class Meta:
        fields = ('id','category','title',
                  'description',
                  'level','teacher','duration',
                  'lectures','stars','price','banner',
                  'img')
        