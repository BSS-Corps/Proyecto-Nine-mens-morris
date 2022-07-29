
import os
import pygame

from Coordenadas import Coordenadas
from Ficha import Ficha
from constants import MUL, player, turn


endGame1 = False
endGame2 = False


class Tablero:
    #global mul
    #mul = 500/843
    coord = Coordenadas()
    ficha = Ficha()

    def __init__(self):
        self.boardImg = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/morrisSmall.png'))
        self.board = list("xxxxxxxxxxxxxxxxxxxxxxxx")
        self.gameComplete = 0
        self.selectMove = False

    def checkEndgame(self, player):
        global endGame
        endGame = False
        cnt = 0
        if(player==0):
            for b in self.board:
                if b == 'B':
                    cnt += 1
            if cnt == 3:
                return True
        elif(player==1):
            for b in self.board:
                if b == 'W':
                    cnt += 1
            if cnt == 3:
                return True
        return False

    def checkGameComplete(self):

        if turn > 18:
            cnt1, cnt2 = 0, 0
            for b in self.board:
                if b == 'B':
                    cnt1 += 1
                if b == 'W':
                    cnt2 += 1
            if cnt2 < 3:
                self.gameComplete = 1
            if cnt1 < 3:
                self.gameComplete = 2


    def drawBoard(self,screen):
        global  lugaresDisponibles, mill, moveLoc

    # midgame
        if self.selectMove:
            if endGame1 and player==0:
                lugaresDisponibles = []
                for loc in range(len(self.board)):
                    if self.board[loc] == 'x':
                        lugaresDisponibles.append(loc)
                        y = MUL*self.coord.coords[loc][1]
                        x = MUL*self.coord.coords[loc][0]
                        screen.blit(self.ficha.highImg,(self.x, self.y))
            elif endGame2 and player==1:
                lugaresDisponibles = []
                for loc in range(len(self.board)):
                    if self.board[loc] == 'x':
                        lugaresDisponibles.append(loc)
                        x = MUL*self.coord.coords[loc][0]
                        y = MUL*self.coord.coords[loc][1]
                        screen.blit(self.ficha.highImg,(self.x, self.y))
            else:
                n = self.coord.neighbors[moveLoc]
                lugaresDisponibles = []
                for j in n:
                    if self.board[j] == 'x':
                        lugaresDisponibles.append(j)
                        x = MUL*self.coord.coords[j][0]
                        y = MUL*self.coord.coords[j][1]
                        screen.blit(self.ficha.highImg,(self.x, self.y))

        for loc in range(len(self.board)):
            if self.board[loc] == 'W':
                self.x = MUL*self.coord.coords[loc][0]
                self.y = MUL*self.coord.coords[loc][1]
                screen.blit(self.ficha.whiteImg,(self.x, self.y))
                print(screen.blit(self.ficha.whiteImg,(self.x, self.y)))
            if self.board[loc] == 'B':
                self.x = MUL*self.coord.coords[loc][0]
                self.y = MUL*self.coord.coords[loc][1]
                screen.blit(self.ficha.blackImg,(self.x, self.y))
                print(screen.blit(self.ficha.blackImg,(self.x, self.y)))

