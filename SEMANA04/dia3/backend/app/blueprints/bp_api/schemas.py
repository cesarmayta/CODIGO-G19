#create your schemas
from utils.db import ma

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('categoria_id','categoria_descripcion')
        
class NivelSchema(ma.Schema):
    class Meta:
        fields = ('nivel_id','nivel_descripcion')
        
class AutorSchema(ma.Schema):
    class Meta:
        fields = ('autor_id','autor_nombre','autor_foto','autor_descripcion')