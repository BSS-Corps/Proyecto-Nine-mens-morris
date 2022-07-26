import imp
import os
import pygame
from Coordenadas import Coordenadas
from Ficha import Ficha

class Tablero:
    global mul 
    mul = 500/843
    coord = Coordenadas()
    ficha = Ficha()
    def __init__(self):
        self.boardImg = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/morrisSmall.png'))
        self.board = list("xxxxxxxxxxxxxxxxxxxxxxxx")
    
    def drawBoard(self,screen):
        for loc in range(len(self.board)):
            if self.board[loc] == 'W':
                self.x = mul*self.coord.coords[loc][0]
                self.y = mul*self.coord.coords[loc][1]
                screen.blit(self.ficha.whiteImg,(self.x, self.y))
            if self.board[loc] == 'B':
                self.x = mul*self.coord.coords[loc][0]
                self.y = mul*self.coord.coords[loc][1]
                screen.blit(self.ficha.blackImg,(self.x, self.y))
