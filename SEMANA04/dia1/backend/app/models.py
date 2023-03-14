from utils.db import db

class Categoria(db.Model):
    __tablename__ = "tbl_categoria"
    
    categoria_id = db.Column(db.Integer,primary_key=True)
    categoria_descripcion = db.Column(db.String(100),nullable=False)
    
    def __init__(self,descripcion):
        self.categoria_descripcion = descripcion
        
class Nivel(db.Model):
    __tablename__ = "tbl_nivel"
    
    nivel_id = db.Column(db.Integer,primary_key=True)
    nivel_descripcion = db.Column(db.String(100),nullable=False)
    
    def __init__(self,descripcion):
        self.nivel_descripcion = descripcion