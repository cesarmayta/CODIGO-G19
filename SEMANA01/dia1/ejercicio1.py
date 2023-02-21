"""
crear un programa que ingrese un numero y cree un cuadrado con * en base al numero
ingresado

ejemplo : num = 5
resultado:

* * * * * 
*       *
*       *
*       *
* * * * *
"""
#ENTRADA
lado = int(input("Ingrese el lado del cuadrado:"))
#PROCESO Y SALIDA
for contador in range(lado):
    if(contador == 0 or contador == (lado-1)):
        print('* '*lado)
    else:
        print('*' + ('  ' * (lado-2)) + ' *' )
