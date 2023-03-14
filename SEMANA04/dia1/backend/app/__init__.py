from flask import Flask
from .models import Categoria,Nivel,Autor,Curso

from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    return app