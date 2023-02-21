import os
opcion = 0
valorCompra = 3.839
valorVenta = 3.849

while(opcion != 3):
    print("="*60)
    print(" "* 10 + "CONVERTIDOR DE MONEDAS VERSION 1.0")
    print("="*60)
    print("""
          OPCIÓN 1 : Convertir de soles a dolares
          OPCIÓN 2 : Convertir de dolares a soles
          OPCIÓN 3 : Salir del programa
          """)
    print("="*60)
    opcion = int(input("Ingrese una opción del menú:"))
    os.system("clear")
    if(opcion == 1):
        print("="*60)
        print("CONVERTIR DE SOLES A DOLARES")
        print("="*60)
        montoOrigen = input("Ingrese monto en soles : ")
        montoDestino = float(montoOrigen) / valorVenta
        monedaDestino = "dolares"
    elif(opcion == 2):
        print("="*60)
        print("CONVERTIR DE DOLARES A SOLES")
        print("="*60)
        montoOrigen = float(input("Ingrese monto en dolares:"))
        montoDestino = montoOrigen * valorCompra
        monedaDestino = "soles"
    elif(opcion == 3):
        print("ADIOS !!!")
    else:
        print("debe ingresar una opción valida ...")
        
    if(opcion == 1 or opcion == 2):
        print("El monto en " + monedaDestino + " es " + str(round(montoDestino,2)))
        input("PRESIONE ENTER PARA CONTINUAR..")
        os.system("clear")
        