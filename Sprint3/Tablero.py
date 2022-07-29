
import os
import pygame

from Coordenadas import Coordenadas
from Ficha import Ficha
from constants import MUL, turn


# endGame1 = False
# endGame2 = False


class Tablero:
    #global mul
    #mul = 500/843
    coord = Coordenadas()
    ficha = Ficha()

    def __init__(self):
        self.boardImg = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/morrisSmall.png'))
        self.board = list("xxxxxxxxxxxxxxxxxxxxxxxx")
        #self.gameComplete = 0
        self.selectMove = False

    # def checkEndgame(self, player):
    #     global endGame
    #     endGame = False
    #     cnt = 0
    #     for b in self.board:
    #         if b == player.simb:
    #             cnt+=1
    #     if cnt == 3:
    #         return True
    #     return False
        # if(player.type ==0):
        #     for b in self.board:
        #         if b == 'B':
        #             cnt += 1
        #     if cnt == 3:
        #         return True
        # elif(player==1):
        #     for b in self.board:
        #         if b == 'W':
        #             cnt += 1
        #     if cnt == 3:
        #         return True
        # return False


    # def checkGameComplete(self):
    #     if turn > 18:
    #         cnt1, cnt2 = 0, 0
    #         for b in self.board:
    #             if b == 'B':
    #                 cnt1 += 1
    #             if b == 'W':
    #                 cnt2 += 1
    #         if cnt2 < 3:
    #             self.gameComplete = 1
    #         if cnt1 < 3:
    #             self.gameComplete = 2


    def drawBoard(self,screen,control,player):
        #global  lugaresDisponibles, mill, moveLoc

    # midgame
        if self.selectMove:
            if control.endGame1 and player.nro==0:
                control.lugaresDisponibles = []
                for loc in range(len(self.board)):
                    if self.board[loc] == 'x':
                        control.lugaresDisponibles.append(loc)
                        self.y = MUL*self.coord.coords[loc][1]
                        self.x = MUL*self.coord.coords[loc][0]
                        screen.blit(self.ficha.highImg,(self.x, self.y))
            elif control.endGame2 and player.nro==1:
                control.lugaresDisponibles = []
                for loc in range(len(self.board)):
                    if self.board[loc] == 'x':
                        control.lugaresDisponibles.append(loc)
                        self.x = MUL*self.coord.coords[loc][0]
                        self.y = MUL*self.coord.coords[loc][1]
                        screen.blit(self.ficha.highImg,(self.x, self.y))
            else:
                self.n = self.coord.neighbors[control.moveLoc]
                control.lugaresDisponibles = []
                for j in self.n:
                    if self.board[j] == 'x':
                        control.lugaresDisponibles.append(j)
                        self.x = MUL*self.coord.coords[j][0]
                        self.y = MUL*self.coord.coords[j][1]
                        screen.blit(self.ficha.highImg,(self.x, self.y))

        for loc in range(len(self.board)):
            if self.board[loc] == 'W':
                self.x = MUL*self.coord.coords[loc][0]
                self.y = MUL*self.coord.coords[loc][1]
                screen.blit(self.ficha.whiteImg,(self.x, self.y))
                #print(screen.blit(self.ficha.whiteImg,(self.x, self.y)))
            if self.board[loc] == 'B':
                self.x = MUL*self.coord.coords[loc][0]
                self.y = MUL*self.coord.coords[loc][1]
                screen.blit(self.ficha.blackImg,(self.x, self.y))
                #print(screen.blit(self.ficha.blackImg,(self.x, self.y)))

