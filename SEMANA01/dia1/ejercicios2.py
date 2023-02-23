"""
EJERCICIOS 02:
INGRESE UN TEXTO Y UN DIVISOR Y LUEGO MUESTRE EL MISMO TEXTO PERO DIVIDO POR EL DIVISOR
EJEMPLO:
INGRESO 
TEXTO = ABCDEFG
DIVISOR = 2
RESULTADO:
AB
CD
EF
G
"""
#ENTRADA
texto = input('ingrese el texto: ')
divisor = int(input('ingrese el divisor: '))
#PROCESO
longitudTexto = len(texto)
for contador in range(0,longitudTexto,divisor):
    #SALIDA
    salida = texto[contador:contador+divisor]
    print(salida)
