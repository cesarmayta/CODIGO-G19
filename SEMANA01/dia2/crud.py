import os
import time
"""
SISTEMA DE MATRICULA DE ALUMNOS
C = CREATE | R = READ | U = UPDATE | D = DELETE
"""
alumno = {
    'nombre':'César Mayta',
    'email':'cesarmayta@gmail.com',
    'celular':'99332233'
}

listaAlumnos = [alumno]

ANCHO = 50

opcion = "0"
while(opcion != "5"):
    time.sleep(1)
    print("="*ANCHO)
    print("PROGRAMA PARA MATRICULA DE ALUMNOS")
    print("="*ANCHO)
    print("""
          [1] REGISTRAR ALUMNO
          [2] MOSTRAR ALUMNOS
          [3] ACTUALIZAR ALUMNO
          [4] ELIMINAR ALUMNO
          [5] SALIR DEL PROGRAMA
          """)
    print("="*ANCHO)
    
    opcion = input("INGRESE UNA OPCIÓN DEL MENU: ")
    os.system("clear")
    if(opcion == "1"):
        print("[1] REGISTRO DE NUEVO ALUMNO")
    elif(opcion == "2"):
        print("[2] RELACIÓN DE ALUMNOS")
    elif(opcion == "3"):
        print("[3] ACTUALIZACIÓN DE ALUMNO")
    elif(opcion == "4"):
        print("[4] ELIMINACIÓN DE ALUMNO")
    elif(opcion == "5"):
        print("[5] ESTA SALIENDO DEL PROGRAMA")
    else:
        print("OPCION NO VALIDA!!!!")