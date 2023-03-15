#create your schemas
from utils.db import ma

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('categoria_id','categoria_descripcion')