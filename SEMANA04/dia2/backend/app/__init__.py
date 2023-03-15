from flask import Flask 
from .blueprints.bp_api import bp_api

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(bp_api)
    
    return app
