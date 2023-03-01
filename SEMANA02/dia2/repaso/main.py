from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    strNombre = request.args.get('nom','nn')
    #return '<h1>Hola {}</h1>'.format(strNombre)
    return f'<h1>Hola {strNombre}</h1>'

@app.route('/saludo')
def saludo():
    strNombre = request.args.get('nombre','')
    return render_template('saludo.html',nombre=strNombre)

@app.route('/peliculas')
def peliculas():
    categoria = request.args.get('cat','nn')
    listaPeliculas = ['Rapidos y furiosos 9','Lord of the Rings 1','Volver al futuro']
    
    context = {
        "categoria":categoria,
        "peliculas":listaPeliculas
    }
    
    return render_template('peliculas.html',**context)

app.run(debug=True)