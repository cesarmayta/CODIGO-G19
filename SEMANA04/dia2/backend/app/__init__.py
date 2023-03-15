from flask import Flask 
from .blueprints.bp_api import bp_api

from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.register_blueprint(bp_api)
    
    return app
