#ejemplo de clases
class Automovil:
    #crear atributos
    def __init__(self,aa,pl,col,mar):
        self.__año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
        
    #crear metodos
    def getAño(self):
        return self.__año
    
    def encender(self):
        print('encender ' + self.marca)
    
    def avanzar(self):
        print('avanzar ' + self.marca)
        
    def acelerar(self):
        print('acelerar ' + self.marca)
        
    def frenar(self):
        print('frenar' + self.marca)
        
#creación de objetos
vw = Automovil(1970,'CH-1234','Amarillo','Volkswagen')
print('se creo el objeto vw con los siguientes datos : ')
print("año : " + str(vw.getAño()))
print("color : " + vw.color)
print("placa : " + vw.placa)
print("marca : " + vw.marca)
vw.encender()

tico = Automovil(1990,'TC-2233','Rojo','Tico')
print('año del tico ' + str(vw.getAño()))
tico.acelerar

        