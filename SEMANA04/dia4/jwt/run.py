from flask import Flask,jsonify,request
from flask_jwt_extended import (
    create_access_token,get_jwt_identity,
    jwt_required,JWTManager)

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "qwerty123"

jwt = JWTManager(app)

@app.route('/')
@jwt_required()
def index():
    context = {
        'content':'ruta publica'
    }
    
    return jsonify(context)


app.run(debug=True)

