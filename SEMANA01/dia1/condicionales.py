#ENTRADA
numero1 = input("Número 1 : ")
numero2 = input("Número 2 : ")
operacion = input("Operación(suma,resta):")

#PROCESO
if(operacion == "suma"):
    resultado = int(numero1) + int(numero2)
elif(operacion == "resta"):
    resultado = int(numero1) - int(numero2)
else:
    resultado = ""

#SALIDA
if(resultado == ""):
    print("no exite la operación solicitada")
else:
    print("el resultado es : " + str(resultado))
