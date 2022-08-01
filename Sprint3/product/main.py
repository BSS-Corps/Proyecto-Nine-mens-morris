import pygame, sys
from button import Button
import os
from Game import Game

sourceFileDir = os.path.dirname(os.path.abspath(__file__))

#f2 = os.path.join(sourceFileDir, '../static/black.png')
pygame.init()
fondo = os.path.join(sourceFileDir, 'assets/Background.png')
fondo2 = os.path.join(sourceFileDir, 'assets/Background2.png')
fuente = os.path.join(sourceFileDir, 'assets/font.ttf')
inicio = os.path.join(sourceFileDir, 'assets/Play Rect.png')
opciones = os.path.join(sourceFileDir, 'assets/Options Rect.png')
salir = os.path.join(sourceFileDir, 'assets/Quit Rect.png')
rectangulo = os.path.join(sourceFileDir, 'assets/Rectangulo.png')
r2 = os.path.join(sourceFileDir, 'assets/R2.png')
#blackImg = pygame.image.load(f2)
SCREEN = pygame.display.set_mode((500, 630))
pygame.display.set_caption("Menu")

BG = pygame.image.load(fondo)
BG2 = pygame.image.load(fondo2)
juego = Game()
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font(fuente, size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG2, (0, 0))
        #SCREEN.fill("black")

        PLAY_TEXT = get_font(20).render("Elija el modo de juego", True, "#F9FCA3")
        
        PLAY_RECT = PLAY_TEXT.get_rect(center=(250, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        AMIGOS = Button(image=pygame.image.load(rectangulo), pos=(250, 230),
                         text_input="Jugador1 vs Jugador 2", font=get_font(15), base_color="#334456", hovering_color="Blue")
        SOLITARIO = Button(image=pygame.image.load(rectangulo), pos=(250, 330),
                         text_input="Jugador1 vs Computadora", font=get_font(15), base_color="#334456", hovering_color="Blue")
        PLAY_BACK = Button(image=pygame.image.load(r2), pos=(250, 460),
                            text_input="BACK", font=get_font(15), base_color="#334456", hovering_color="Green")

        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        AMIGOS.changeColor(PLAY_MOUSE_POS)
        SOLITARIO.changeColor(PLAY_MOUSE_POS)
        AMIGOS.update(SCREEN)
        SOLITARIO.update(SCREEN)
        PLAY_BACK.update(SCREEN)


        for event in pygame.event.get():
            
            juego.game.chekGameOver(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if AMIGOS.checkForInput(PLAY_MOUSE_POS):
                    juego.oponente_real() #cambiarcheckForInput

                if SOLITARIO.checkForInput(PLAY_MOUSE_POS):
                    juego.oponente_virtual() 

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(30).render("MENU PRINCIPAL", True, "#F9FCA3")
        MENU_RECT = MENU_TEXT.get_rect(center=(260, 100))

        PLAY_BUTTON = Button(image=pygame.image.load(inicio), pos=(260, 250), 
                            text_input="JUGAR", font=get_font(25), base_color="#d4fc79", hovering_color="White")
       
        QUIT_BUTTON = Button(image=pygame.image.load(salir), pos=(260, 450), 
                            text_input="SALIR", font=get_font(25), base_color="#d4fc79", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            juego.game.chekGameOver(event)
            # if event.type == pygame.QUIT:
            #     pygame.quit()
            #     sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                # if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                #     options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()