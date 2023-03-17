import datetime
from flask import Flask,jsonify,request
from flask_jwt_extended import (
    create_access_token,get_jwt_identity,
    jwt_required,JWTManager)

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "qwerty12f3"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=1)

jwt = JWTManager(app)

@app.route('/')
@jwt_required()
def index():
    context = {
        'content':'ruta publica'
    }
    
    return jsonify(context)

@app.route('/login',methods=["POST"])
def login():
    usuario = request.json.get("usuario",None)
    password = request.json.get("password",None)
    
    if usuario == "admin" and password == "1234":
        token = create_access_token({"usuario":"admin"})
    else:
        token = "invalid"
    
    context = {
        'content':token
    }
    
    return jsonify(context)


app.run(debug=True)

