opcion = 0
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
    if(opcion == 1):
        print("CONVERTIR DE SOLES A DOLARES")
    elif(opcion == 2):
        print("CONVERTIR DE DOLARES A SOLES")
    elif(opcion == 3):
        print("ADIOS !!!")
    else:
        print("debe ingresar una opción valida ...")
        