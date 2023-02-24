class Persona:
    def __init__(self,nom,ema):
        self.nombre = nom
        self.email = ema
        
    def mostrar(self):
        print("Nombre : " + self.nombre)
        print("Email : " + self.email)
    
class Alumno(Persona):
    
    def __init__(self,nom,ema,nota):
        super().__init__(nom,ema)
        self.nota = nota
    
    def mostrar(self):
        print("*" * 20 + "DATOS DEL ALUMNO")
        super().mostrar()
        print("Nota : " + str(self.nota))
        
class Profesor(Persona):
    
    def __init__(self,nom,ema,esp):
        super().__init__(nom,ema)
        self.especialidad = esp
        
    def mostrar(self):
        print("*" * 20 + "DATOS DEL PROFESOR")
        super().mostrar()
        print("Especialidad :" + self.especialidad)
        
alumno1 = Alumno('Carlos tello','ctello@gmail.com',11)
alumno1.mostrar()

profesor1 = Profesor('César Mayta','cesarmayta@gmail.com','Backend')
profesor1.mostrar()