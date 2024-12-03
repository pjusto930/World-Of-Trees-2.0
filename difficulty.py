# Importo pygame y sistema
import pygame, sys
from pygame.locals import *
from button import Button
import sound
import avanzado

# Inicializo pygame
pygame.init()

# Creo y seteo valores a la pantalla
pantalla = pygame.display.set_mode((1300, 690))
pygame.display.set_caption("World Of Trees")  # Título de la ventana

# Declaro e inserto el icono de la ventana
icono = pygame.image.load("assets/images/items/planta.png")
pygame.display.set_icon(icono)

# Fondo del menú
menuBg = pygame.image.load("assets/images/fondos/fondlevel.png")

btnPrincipiante = pygame.image.load("assets/images/menu/beginner.png")
btnPrincipiante = pygame.transform.scale(btnPrincipiante, (700, 129))

btnAvanzado = pygame.image.load("assets/images/menu/advanced.png")
btnAvanzado = pygame.transform.scale(btnAvanzado, (700, 130))

backArrow = pygame.image.load("assets/images/menu/backArrow.png")
backArrow = pygame.transform.scale(backArrow, (600, 150))

# Fuente
def get_font(size):
    return pygame.font.Font("assets/Font/font.ttf", size)

def difi():

    sound.sound_menu()  # Reproduce el soundtrack del primer nivel

    def back():
        from sound import sound_clic1
        sound_clic1()  # Reproduce el sonido del botón
        from startere import main_menu
        main_menu()

    # Función de la pantalla play
    def jugar():
        from sound import sound_Button
        sound_Button()  # Reproduce el sonido del botón
        from diffStarter import levels_p
        levels_p()  # Mando llamar la función play del archivo principiante

    # Función de la pantalla opciones    
    def options():
        from sound import sound_Button
        sound_Button()  # Reproduce el sonido del botón
        from diffAdvanced import levels_a
        levels_a()  # Mando llamar la función play del archivo avanzado

    # Función del menú principal
    def dif_menu():
        # Variables para el desplazamiento del fondo
        x = 0  # Posición inicial del fondo
        velocidad_fondo = 0.4  # Velocidad de desplazamiento del fondo

        while True:
            # Desplazamiento horizontal del fondo
            x -= velocidad_fondo  # Mueve el fondo hacia la izquierda

            # Calcula la posición relativa del fondo para hacer un bucle infinito
            x_relativa = x % menuBg.get_rect().width
            pantalla.blit(menuBg, (x_relativa - menuBg.get_rect().width, 0))
            pantalla.blit(menuBg, (x_relativa, 0))

            # Después de dibujar el fondo, ahora se dibujan los botones y el texto
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(25).render("", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(200, 300))

            PLAY_BUTTON = Button(image=btnPrincipiante, pos=(650, 300), 
                                text_input="", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=btnAvanzado, pos=(650, 450), 
                                text_input="", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=backArrow, pos=(100, 670), 
                                text_input="", font=get_font(22), base_color="#d7fcd4", hovering_color="White")

            pantalla.blit(MENU_TEXT, MENU_RECT)

            # Agregar hoverEffect para los botones
            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.hoverEffect(MENU_MOUSE_POS)  # Aplicar el efecto de hover
                button.update(pantalla)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        jugar()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        back()

            pygame.display.update()

    dif_menu()
