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
        
class CursoSchema(ma.Schema):
    class Meta:
        fields = ('curso_id','curso_titulo','curso_descripcion',
                  'curso_fecharegistro',
                  'categoria_id','nivel_id','autor_id',
                  'curso_imagen','curso_duracion','curso_precio','curso_clases','cat.categoria_descripcion')