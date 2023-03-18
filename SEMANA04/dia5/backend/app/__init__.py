from flask import Flask
from flask_cors import CORS 
from .blueprints.bp_api import bp_api
from .blueprints.bp_auth import bp_auth

from flask_jwt_extended import JWTManager

from .config import Config

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    jwt = JWTManager(app)
    
    app.register_blueprint(bp_api)
    app.register_blueprint(bp_auth)
    
    return app
