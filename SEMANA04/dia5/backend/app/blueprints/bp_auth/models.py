from utils.db import db

class Usuario(db.Model):
    __tablename__ = "tbl_usuario"
    
    usuario_id = db.Column(db.Integer,primary_key=True)
    usuario_nombre = db.Column(db.String(100),nullable=False)
    usuario_password = db.Column(db.String(254),nullable=False)
    
    def __init__(self,username,password):
        self.usuario_nombre = username
        self.usuario_password = password
        
    @staticmethod
    def get_all():
        return Usuario.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)
    
    def save(self):
        if not self.usuario_id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        