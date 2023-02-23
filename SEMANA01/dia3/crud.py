import os
import time
from tabulate import tabulate
from librerias.libAlumnos import *

"""
SISTEMA DE MATRICULA DE ALUMNOS
C = CREATE | R = READ | U = UPDATE | D = DELETE
"""
#cargamos alumnos del archivo csv
listaAlumnos = []
f = open('alumnos.csv','r')
strAlumnos = f.read()
f.close()

listaAlumnosCSV = strAlumnos.splitlines()
for strAlumnoCSV in listaAlumnosCSV:
    listaAlumnoInvidualCSV = strAlumnoCSV.split(';')
    dictAlumnoCSV = {
        'nombre':listaAlumnoInvidualCSV[0],
        'email':listaAlumnoInvidualCSV[1],
        'celular':listaAlumnoInvidualCSV[2]
    }
    listaAlumnos.append(dictAlumnoCSV)
    
ANCHO = 50

opcion = "0"
while(opcion != "5"):
    time.sleep(1)
    mostrarMenu(ANCHO)
    
    opcion = input("INGRESE UNA OPCIÓN DEL MENU: ")
    os.system("clear")
    if(opcion == "1"):
        print("[1] REGISTRO DE NUEVO ALUMNO")
        listaAlumnos.append(insertarAlumno())
    elif(opcion == "2"):        
        cabeceras = ["NOMBRE","EMAIL","CELULAR"]
        mostrarListado(listaAlumnos,cabeceras)
        input("PRESIONE ENTER PARA CONTINUAR...")
    elif(opcion == "3"):
        print("[3] ACTUALIZACIÓN DE ALUMNO")
        valorBusqueda = input('INGRESE EL EMAIL DEL ALUMO A ACTUALIZAR : ')
        posicionBusqueda = -1
        for posicion in range(len(listaAlumnos)):
            dicAlumno = listaAlumnos[posicion]
            for clave,valor in dicAlumno.items():
                if(clave == "email" and valor == valorBusqueda):
                    posicionBusqueda = posicion
                    break
                
        if (posicionBusqueda == -1):
            print("NO SE ENCONTRO EL ALUMNO SOLICITADO")
        else:
            print("""ALUMNO ENCONTRADO : 
                  """ + listaAlumnos[posicionBusqueda].get("nombre") + """ 
                  """ + listaAlumnos[posicionBusqueda].get("email") + """ 
                  """ + listaAlumnos[posicionBusqueda].get("celular"))
            
            nombre = input('NUEVO NOMBRE: ')
            email = input('NUEVO EMAIL: ')
            celular = input('NUEVO CELULAR: ')
            
            dicAlumnoEditar = {
                'nombre':nombre,
                'email':email,
                'celular':celular
            }
            listaAlumnos[posicionBusqueda] = dicAlumnoEditar
            print('ALUMNO ACTUALIZADO !!!')
            
    elif(opcion == "4"):
        print("[4] ELIMINACIÓN DE ALUMNO")
        valorBusqueda = input('INGRESE EL EMAIL DEL ALUMO A ACTUALIZAR : ')
        posicionBusqueda = -1
        for posicion in range(len(listaAlumnos)):
            dicAlumno = listaAlumnos[posicion]
            for clave,valor in dicAlumno.items():
                if(clave == "email" and valor == valorBusqueda):
                    posicionBusqueda = posicion
                    break
                
        if (posicionBusqueda == -1):
            print("NO SE ENCONTRO EL ALUMNO A ELIMINAR")
        else:
            listaAlumnos.pop(posicionBusqueda)
            print("ALUMNO ELIMINADO !!!")
    elif(opcion == "5"):
        print("[5] ESTA SALIENDO DEL PROGRAMA")
        #grabar los cambios de la lista de alumnos en el archivo csv
        strAlumnos = ""
        for dictAlumno in listaAlumnos:
            for clave,valor in dictAlumno.items():
                strAlumnos += valor
                if clave != 'celular':
                    strAlumnos += ';'
                else:
                    strAlumnos += '\n'
        #print(strAlumnos)
        fSalida = open('alumnos.csv','w')
        fSalida.write(strAlumnos)
        fSalida.close()
    else:
        print("OPCION NO VALIDA!!!!")