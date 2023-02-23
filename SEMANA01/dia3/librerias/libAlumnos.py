"""
LIBRERIA DE FUNCIONES PARA EL CRUD DE ALUMNOS
"""
from tabulate import tabulate

def mostrarMenu(ancho):
    print("="*ancho)
    print("PROGRAMA PARA MATRICULA DE ALUMNOS")
    print("="*ancho)
    print("""
          [1] REGISTRAR ALUMNO
          [2] MOSTRAR ALUMNOS
          [3] ACTUALIZAR ALUMNO
          [4] ELIMINAR ALUMNO
          [5] SALIR DEL PROGRAMA
          """)
    print("="*ancho)
    
def insertarAlumno():
    nombre = input("NOMBRE : ")
    email = input("EMAIL : ")
    celular = input("CELULAR : ")
    dicNuevoAlumno = {
        'nombre':nombre,
        'email':email,
        'celular':celular
    }
    return dicNuevoAlumno

def mostrarListado(listado,cabeceras):
    tabla = [dato.values() for dato in listado]
    print(tabulate(tabla,headers=cabeceras,tablefmt="grid"))
