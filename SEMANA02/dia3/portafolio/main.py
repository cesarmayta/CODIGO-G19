from flask import Flask,request,render_template
from GitHubProfile import GitHubProfile
from FirebaseAdmin import FirebaseAdmin

app = Flask(__name__)

fb = FirebaseAdmin()

@app.route('/')
def index():
    perfil = GitHubProfile()
    context = {
        'nombre':perfil.nombre,
        'imagen':perfil.imagen,
        'biografia':perfil.biografia,
        'ubicacion':perfil.ubicacion,
        'github':perfil.github,
        'twitter':perfil.twitter
    }
    return render_template('index.html',**context)

@app.route('/portafolio')
def portafolio():
    listaProyectos = fb.getCollection('proyectos')
    
    context = {
        'proyectos':listaProyectos
    }
    
    return render_template('portafolio.html',**context)
    
@app.route('/acercade')
def acercade():
    return render_template('acercade.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

app.run(debug=True)