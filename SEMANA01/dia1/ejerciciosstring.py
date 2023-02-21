mensaje = "Hola Mundo"
#len : obtiene la longitud de una cadena de texto
print(len(mensaje))
#buscar un texto dentro de otro
mensaje2 = mensaje.find("p")
print(mensaje2)
#convertir mayusculas
print(mensaje.upper())
#convertir minusculas
print(mensaje.lower())
#reemplazar un texto
mensaje3 = mensaje.replace("l",'PP')
print(mensaje3)

##cortar una cadena cortar
mensaje4 = mensaje[2:7]
print(mensaje4)

for letra in mensaje:
    print(letra)
    
mensaje5 = mensaje[:5]
print(mensaje5)

mensaje6 = mensaje[::-1]
print(mensaje6)