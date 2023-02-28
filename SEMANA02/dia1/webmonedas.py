from flask import Flask,request

app =  Flask(__name__)

@app.route('/')
def index():
    httpResponse = "<center><h1>TIPOS DE CAMBIO DEL DÍA</h1></center>"
    return httpResponse

app.run(debug=True)