class Usuario:
    __email = 'cesarmayta@gmail.com'
    __password = 'qwerty123'
    
    #def __init__(self):
    #    pass
    
    def login(self,email,password):
        if(self.__email == email and self.__password == password):
            print("Bienvenido " + self.__email)
        else:
            print("datos de acceso incorrectos")
            
usuario1 = Usuario()
usuario1.login('cesarmayta@gmail.com','123')

usuario2 = Usuario()
usuario2.login('cesarmayta@gmail.com','qwerty123')


        