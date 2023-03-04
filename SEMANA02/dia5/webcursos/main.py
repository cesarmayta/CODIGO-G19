from flask import Flask,render_template,request
from flask_mysqldb import MySQL 


app = Flask(__name__)

#CONFIGURAMOS LA CONEXIÓN A LA BASE DE DATOS
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cursos'

mysql  = MySQL(app)
print("conectado a la base de datos")

@app.route('/')
def index():
    #consultamos los cursos
    curCursos = mysql.connection.cursor()
    sqlCursos = "select id,nombre from curso"
    curCursos.execute(sqlCursos)
    dataCursos = curCursos.fetchall()
    curCursos.close()
    #creamos sentencia sql para las notas de los cursos
    
    sqlNotas = "select a.nombre as alumno\n"
    for curso in dataCursos:
        sqlNotas += ",COALESCE(n"+str(curso[0])+".nota,0) as '"+curso[1]+"'"
    sqlNotas += ",AVG(COALESCE(n.nota,0)) as PROMEDIO"
    sqlNotas += " from alumno a\n"
    sqlNotas += " INNER JOIN alumno_curso n ON n.alumno_id = a.id"
    for curso in dataCursos:
        sqlNotas += " LEFT JOIN alumno_curso n"+str(curso[0])+" ON n"+str(curso[0])+".alumno_id = a.id and n"+str(curso[0])+".curso_id = "+str(curso[0])+""
    sqlNotas += " GROUP BY a.nombre"
    for curso in dataCursos:
        sqlNotas += ",n"+str(curso[0])+".nota"
    sqlNotas += ";"
    
    #creamos el cursor para ejecutar la consulta
    curNotas = mysql.connection.cursor()
    curNotas.execute(sqlNotas)
    dataNotas = curNotas.fetchall()
    curNotas.close()
    
    print(dataNotas)
    
    context = {
        'cursos':dataCursos,
        'notas':dataNotas
    }
    return render_template('index.html',**context)

app.run(debug=True)