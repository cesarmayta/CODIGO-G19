def decorador(func):
    def envoltura():
        print('esto es un decorador que se añade a la función principal')
        func()
    return envoltura

def mensaje():
    print('hola esto es una función')
    
#mensaje = decorador(mensaje)
#mensaje()
@decorador
def mensaje():
    print('hola mundo')
    
mensaje()

def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mostrarTexto(texto):
    return 'texto : ' + texto

print(mostrarTexto('hola mundo con decoradores'))
