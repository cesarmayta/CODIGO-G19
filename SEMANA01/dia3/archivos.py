#abrir archivo con permisos de escritura
f = open('alumnos.txt','w')
f.write('cesar mayta,cesarmayta@gmail.com,90898998')
f.write('\nana lopez,ana@gmail.com,908098098')
f.close()

#abrir archivo en modo append para adicionar información
fa = open('alumnos.txt','a')
fa.write('\n')
fa.write('jorge perez,jorge@gmail.com,99828282')
fa.close()

#abrir archivo con permisos de lectura
fr = open('alumnos.txt','r')
dataAlumnos = fr.read()
print(dataAlumnos)
fr.close()
print(type(dataAlumnos))

#convertir texto en una lista de diccionarios
listaAlumnos = dataAlumnos.splitlines()
print(listaAlumnos)
print(type(listaAlumnos))
print(listaAlumnos[0])

listaAlumnosFinal = []
for strAlumno in listaAlumnos:
    listaAlumnoIndividual = strAlumno.split(',')
    #print(listaAlumnoIndividual)
    dicAlumno = {
        'nombre':listaAlumnoIndividual[0],
        'email':listaAlumnoIndividual[1],
        'celular':listaAlumnoIndividual[2]
    }
    listaAlumnosFinal.append(dicAlumno)
    
print(listaAlumnosFinal)