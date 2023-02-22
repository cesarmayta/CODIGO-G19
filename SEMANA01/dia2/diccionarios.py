capitales = {
    'Perú':'Lima',
    'Ecuador':'Quito',
    'Chile':'Santiago',
    'Uruguay':'Montevideo'
}

print(capitales)
#para agregar un nuevo valor
nuevaCapital = {
    'Brasil':'Brasilia'
}

capitales.update(nuevaCapital)
print(capitales)

"""pais = input('Ingrese el pais:')
capital = capitales.get(pais)
print("la capital de ",pais," es ",capital)"""
#actualizar diccionario
capitales.update({'Chile':'Arica'})
print(capitales)

#eliminar dato de un diccionario
capitales.pop('Chile')
print(capitales)

capitalEliminada = capitales.pop('Brasil','no existe')
print('Capital Eliminada :  ' + capitalEliminada)

##recorrer diccionarios
#recorrer claves
for clave in capitales.keys():
    print(clave)
#recorrer valores
for valor in capitales.values():
    print(valor)
#recorrer clave y valor
for clave,valor in capitales.items():
    print('la capital de ' + clave + ' es ' + valor)