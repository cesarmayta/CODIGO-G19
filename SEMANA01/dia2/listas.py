dias = ['lunes','martes',0,True,0.45]

print(dias)
print(dias[0:2])
#agregar un valor a lista
dias.append("miercoles")
print(dias)
#eliminar un valor de la lista
dias.pop(3)
print(dias)
#eliminar varios valores de un alista
del dias[2:4]
print(dias)
#actualizar un valor de la lista
dias.append("j")
print(dias)
dias[3] = "jueves"
print(dias)

#recorrer una lista
for contador in range(len(dias)):
    print(dias[contador])
    
for dia in dias:
    print(dia)


