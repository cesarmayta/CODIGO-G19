from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return  '<center><h1>BIENVENIDO A MI WEB CON FLASK</h1></center>'

app.run()