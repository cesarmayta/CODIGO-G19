import pygame
import sys

ANCHO = 640
ALTO = 480
FONDO = (0,0,64)

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
        if self.rect.bottom >= ALTO or self.rect.top <= 0:
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


pantalla = pygame.display.set_mode((ANCHO,ALTO))

pygame.display.set_caption('Juego en python de codigo g19')

#crear un reloj para hacer que la bolita se mueva mas lento
reloj = pygame.time.Clock()
#ajustar repetición de eventos de presion de tecla
pygame.key.set_repeat(30)

#CREAMOS LOS OBJETOS DEL VIDEOJUEGO
bolita = Bolita()
jugador = Paleta()

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
    
    #Pintamos la pantalla
    pantalla.fill(FONDO)
    #Dibujar la bolita en la pantalla
    pantalla.blit(bolita.image,bolita.rect)
    #Dibujar al jugador en la pantalla
    pantalla.blit(jugador.image,jugador.rect)
    #actualizar los elementos en la pantalla
    pygame.display.flip()