from turtle import Screen
import pygame, sys
import coordenada

#Dimensiones
WIDTH = 800
HEIGHT = 715
LINE_WIDTH = 15

#Colores
RED = (255,0,0)
BG_COLOR = (28,170,156)
LINE_COLOR = (23,145,135)

#Inicializacion
pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("Nine men's morris")
screen.fill( BG_COLOR )

#Coordenadas 
v1 = coordenada.Coordenada(100,50)
v2 = coordenada.Coordenada(400,50)
v3 = coordenada.Coordenada(700,50)
v4 = coordenada.Coordenada(200,150)
v5 = coordenada.Coordenada(400,150)
v6 = coordenada.Coordenada(600,150)
v7 = coordenada.Coordenada(300,250)
v8 = coordenada.Coordenada(400,250)
v9 = coordenada.Coordenada(500,250)
v10 = coordenada.Coordenada(100,350)
v11 = coordenada.Coordenada(200,350)
v12 = coordenada.Coordenada(300,350)
v13 = coordenada.Coordenada(500,350)
v14 = coordenada.Coordenada(600,350)
v15 = coordenada.Coordenada(700,350)
v16 = coordenada.Coordenada(300,450)
v17 = coordenada.Coordenada(400,450)
v18 = coordenada.Coordenada(500,450)
v19 = coordenada.Coordenada(200,550)
v20 = coordenada.Coordenada(400,550)
v21 = coordenada.Coordenada(600,550)
v22 = coordenada.Coordenada(100,650)
v23 = coordenada.Coordenada(400,650)
v24 = coordenada.Coordenada(700,650)

class Tablero:
        
    vertices = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24]

    def draw_lines(self):
        #BORDES
        #Horizontal Superior
        pygame.draw.line( screen, LINE_COLOR, v1.get_coordenada() , v3.get_coordenada(), LINE_WIDTH )
        #Horizontal Inferior
        pygame.draw.line( screen, LINE_COLOR, v22.get_coordenada(),v24.get_coordenada(), LINE_WIDTH )
        #Vertical Izquierdo
        pygame.draw.line( screen, LINE_COLOR, v1.get_coordenada(),v22.get_coordenada(), LINE_WIDTH )
        #Vertical Derecho
        pygame.draw.line( screen, LINE_COLOR, v3.get_coordenada(),v24.get_coordenada(), LINE_WIDTH )
        
        #Cuadrado interno 1
        #Horizontal Superior
        pygame.draw.line( screen, LINE_COLOR, v4.get_coordenada(),v6.get_coordenada(), LINE_WIDTH )
        #Horizontal Inferior
        pygame.draw.line( screen, LINE_COLOR, v19.get_coordenada(),v21.get_coordenada(), LINE_WIDTH )
        #Vertical Izquierdo
        pygame.draw.line( screen, LINE_COLOR, v4.get_coordenada(),v19.get_coordenada(), LINE_WIDTH )
        #Vertical Derecho
        pygame.draw.line( screen, LINE_COLOR, v6.get_coordenada(),v21.get_coordenada(), LINE_WIDTH )