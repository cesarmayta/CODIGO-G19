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
    
def buscarPosicionEnListado(valorBusqueda,listado):
    posicionBusqueda = -1
    for posicion in range(len(listado)):
        dicDato = listado[posicion]
        for clave,valor in dicDato.items():
            if(clave == "email" and valor == valorBusqueda):
                posicionBusqueda = posicion
                break
    return posicionBusqueda

def actualizar(**kwargs):
    listado = kwargs.get('listAct')
    dicActualizar = kwargs.get('dicAct')
    posicion = kwargs.get('indexAct')
    
    listado[posicion] = dicActualizar
    
    return listado

def cargarDatos(strDatos,separador,columnas):
    listaResultado = []
    listadoGeneral = strDatos.splitlines()
    for strRegistro in listadoGeneral:
        listaRegistro = strRegistro.split(separador)
        dictRegistro = {}
        for cont in range(len(columnas)):
            dicDato = {columnas[cont] : listaRegistro[cont]}
            dictRegistro.update(dicDato)
        listaResultado.append(dictRegistro)
    return listaResultado

def grabarDatos(listado,separador,ultimaClave):
    strResultado = ""
    for dictRegistro in listado:
        for clave,valor in dictRegistro.items():
            strResultado += valor
            if clave != ultimaClave:
                strResultado += separador
            else:
                strResultado += '\n'
    return strResultado