#create your models
from utils.db import db

class Categoria(db.Model):
    __tablename__ = "tbl_categoria"
    
    categoria_id = db.Column(db.Integer,primary_key=True)
    categoria_descripcion = db.Column(db.String(100),nullable=False)
    
    def __init__(self,descripcion):
        self.categoria_descripcion = descripcion
        
    @staticmethod
    def get_all():
        return Categoria.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Categoria.query.get(id)
    
    def save(self):
        if not self.categoria_id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
        
class Nivel(db.Model):
    __tablename__ = "tbl_nivel"
    
    nivel_id = db.Column(db.Integer,primary_key=True)
    nivel_descripcion = db.Column(db.String(100),nullable=False)
    
    def __init__(self,descripcion):
        self.nivel_descripcion = descripcion
        
    @staticmethod
    def get_all():
        return Nivel.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Nivel.query.get(id)
    
    def save(self):
        if not self.nivel_id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
class Autor(db.Model):
    __tablename__ = "tbl_autor"
    
    autor_id = db.Column(db.Integer,primary_key=True)
    autor_nombre = db.Column(db.String(200),nullable=False)
    autor_foto = db.Column(db.String(200),nullable=True)
    autor_descripcion = db.Column(db.Text)
    
    def __init__(self,nombre,foto,descripcion):
        self.autor_nombre = nombre
        self.autor_foto = foto
        self.autor_descripcion = descripcion
        
    @staticmethod
    def get_all():
        return Autor.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Autor.query.get(id)
    
    def save(self):
        if not self.autor_id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        
class Curso(db.Model):
    __tablename__ =  "tbl_curso"
    
    curso_id = db.Column(db.Integer,primary_key=True)
    curso_titulo = db.Column(db.String(200),nullable=False)
    curso_descripcion = db.Column(db.Text)
    curso_fecharegistro = db.Column(db.Date,nullable=False)
    categoria_id = db.Column(db.Integer,db.ForeignKey("tbl_categoria.categoria_id"))
    nivel_id = db.Column(db.Integer,db.ForeignKey("tbl_nivel.nivel_id"))
    autor_id = db.Column(db.Integer,db.ForeignKey("tbl_autor.autor_id"))
    
    def __init__(self,titulo):
        self.curso_titulo = titulo