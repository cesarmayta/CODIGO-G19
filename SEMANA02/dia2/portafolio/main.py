from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    nombre = 'CESAR MAYTA'
    context = {
        'nombre':nombre
    }
    return render_template('index.html',**context)

app.run(debug=True)