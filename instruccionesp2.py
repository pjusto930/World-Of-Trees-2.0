# Importo pygame y sistema
import pygame, sys
from pygame.locals import *
from button import Button
import constantes
import sound

# Inicializo pygame
pygame.init()

# Creo y seteo valores a la pantalla
pantalla = pygame.display.set_mode((1300, 690))
pygame.display.set_caption("Hungry Jump")  # Título de la ventana

# Declaro e inserto el icono de la ventana
icono = pygame.image.load("assets/images/items/planta.png")
pygame.display.set_icon(icono)

# Fuente
def get_font(size):
    return pygame.font.Font("assets/Font/font.ttf", size)

def instrucciones():

    # Fondo del menú
    hoja = pygame.image.load("assets/images/menu/Instrucciones.png")
    hoja = pygame.transform.scale(hoja, (constantes.anchoVentana, constantes.altoVentana))

    while True:
        pantalla.blit(hoja, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                import lvl2
                lvl2.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                import lvl2
                lvl2.play()

        pygame.display.update()