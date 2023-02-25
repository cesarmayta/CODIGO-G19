import pygame
import sys
import time

ANCHO = 640
ALTO = 480
FONDO = (0,0,64)

pygame.init()

#### CREAMOS OBJETOS DEL VIDEJUEGO
class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #cargar la imagen
        self.image = pygame.image.load('imagenes/bolita.png')
        #obtener el rectangulo de la imagen
        self.rect = self.image.get_rect()
        #posición inicial de la bolita en la pantalla
        #para cemtrarlo en la pantalla
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        self.speed = [3,3]
        
    def update(self):
        #verificar si la bolita se sale de la pantalla
        #if self.rect.bottom >= ALTO or self.rect.top <= 0:
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        self.rect.move_ip(self.speed)
        
class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #cargar imagen
        self.image = pygame.image.load('imagenes/paleta.png')
        #obtenemos rectangulo
        self.rect = self.image.get_rect()
        
        #posición inicial de la palet centraa solo en el eje x de la pantalla
        self.rect.midbottom = (ANCHO /2,ALTO - 20)
        #establecemos el speed inicial
        self.speed = [0,0]
        
    def update(self,evento):
        #buscar si se presionó la tecla de la flecha izquierda
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5,0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [5,0]
        else:
            self.speed = [0,0]
            
        self.rect.move_ip(self.speed)

class Ladrillo(pygame.sprite.Sprite):
    def __init__(self,posicion):
        pygame.sprite.Sprite.__init__(self)
        #cargar imagen
        self.image = pygame.image.load('imagenes/ladrillo.png')
        #obtener el rectangulo
        self.rect = self.image.get_rect()
        #posición inicial
        self.rect.topleft = posicion

class Muro(pygame.sprite.Group):
    def __init__(self,cantidadLadrillos):
        pygame.sprite.Group.__init__(self)
        
        pos_x = 0
        pos_y = 20
        for i in range(cantidadLadrillos):
            ladrillo = Ladrillo((pos_x,pos_y))
            self.add(ladrillo)
            
            pos_x += ladrillo.rect.width
            if pos_x >= ANCHO:
                pos_x = 0
                pos_y += ladrillo.rect.height
        

############### FUNCIONES PARA ETAPAS DEL JUEGO

def juego_terminado():
    fuente = pygame.font.SysFont('Arial',72)
    texto = fuente.render('GAME OVER',True,(255,255,255))
    texto_rect = texto.get_rect()
    texto_rect.center = [ANCHO / 2, ALTO / 2]
    pantalla.blit(texto,texto_rect)
    pygame.display.flip()
    #pausar por 3 segundos
    pygame.mixer.Sound.play(sonido_game_over)
    time.sleep(5)
    
    sys.exit()
    
def mostrar_puntuacion():
    fuente = pygame.font.SysFont('Consolas',20)
    texto = fuente.render(str(puntuacion).zfill(5),True,(255,255,255))
    texto_rect = texto.get_rect()
    texto_rect.topleft = [0,0]
    pantalla.blit(texto,texto_rect)



pantalla = pygame.display.set_mode((ANCHO,ALTO))

pygame.display.set_caption('Juego en python de codigo g19')

#crear un reloj para hacer que la bolita se mueva mas lento
reloj = pygame.time.Clock()
#ajustar repetición de eventos de presion de tecla
pygame.key.set_repeat(30)

#CREAMOS LOS OBJETOS DEL VIDEOJUEGO
bolita = Bolita()
jugador = Paleta()
muro = Muro(50)

puntuacion = 0

#carga de sonidos del videojuego
sonido_colision = pygame.mixer.Sound('sonidos/colision.ogg')
sonido_colision_muro = pygame.mixer.Sound('sonidos/colision_muro.ogg')
sonido_game_over = pygame.mixer.Sound('sonidos/game_over.ogg')

while True:
    #establacer el tiempo del reloj
    reloj.tick(60)
    #bucle para recorrer los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            #cerrar videojuego
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            jugador.update(evento)
    
    #movemos la bolita
    bolita.update()
    
    ############### COLISIONES #################
    #Colisión entre bolita y jugador
    if pygame.sprite.collide_rect(bolita,jugador):
        bolita.speed[1] = -bolita.speed[1]
        pygame.mixer.Sound.play(sonido_colision)
        
    #colisión de la bolita con el muro
    lista = pygame.sprite.spritecollide(bolita,muro,False)
    if lista:
        ladrillo = lista[0]
        cx = bolita.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita.speed[0] = -bolita.speed[0]
        else:
            bolita.speed[1] = -bolita.speed[1]
        muro.remove(ladrillo)
        pygame.mixer.Sound.play(sonido_colision_muro)
        puntuacion += 10
    
    
    #revisar si la bolita sale de la pantalla
    if bolita.rect.top > ALTO:
        juego_terminado()
    
    
    #Pintamos la pantalla
    pantalla.fill(FONDO)
    #mostramos puntuación
    mostrar_puntuacion()
    #Dibujar la bolita en la pantalla
    pantalla.blit(bolita.image,bolita.rect)
    #Dibujar al jugador en la pantalla
    pantalla.blit(jugador.image,jugador.rect)
    #dibujamos el muro
    muro.draw(pantalla)
    
    #actualizar los elementos en la pantalla
    pygame.display.flip()