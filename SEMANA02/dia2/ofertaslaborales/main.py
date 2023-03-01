from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    listaOfertas = [
        {
            "titulo":"Python Developer",
            "imagen":"https://beapythondev.files.wordpress.com/2019/06/python.png?w=365&h=365&crop=1",
            "descripcion":"Buscamos python developer con experiencia en flask para proyecto grande"
        },
        {
            "titulo":"NodeJs Developer",
            "imagen":"https://miro.medium.com/max/1400/1*ODU5V_oAmYmzvZ1wIw3rDw.png",
            "descripcion":"Buscamos NodeJs developer con experiencia en flask para proyecto grande"
        },
        {
            "titulo":"React Developer",
            "imagen":"https://sigdeletras.com/images/blog/202004_react_leaflet/react.png",
            "descripcion":"Buscamos React developer con experiencia en flask para proyecto grande"
        }
    ]
    
    context = {
        "ofertas":listaOfertas
    }
    return render_template('index.html',**context)

@app.route('/detalle')
def detalle():
    return render_template('detalle.html')

app.run(debug=True)

