import pygame
import sys

ANCHO = 640
ALTO = 480

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


pantalla = pygame.display.set_mode((ANCHO,ALTO))

pygame.display.set_caption('Juego en python de codigo g19')

#CREAMOS LOS OBJETOS DEL VIDEOJUEGO
bolita = Bolita()

while True:
    #bucle para recorrer los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            #cerrar videojuego
            sys.exit()
    
    #Dibujar la bolita en la pantalla
    pantalla.blit(bolita.image,bolita.rect)
    #actualizar los elementos en la pantalla
    pygame.display.flip()