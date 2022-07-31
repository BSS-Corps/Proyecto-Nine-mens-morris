import pygame
from Rules import Rules
from Player import Player

class FaseTemprana():
    
    def __init__(self,player,board,rules,clickables):
        self.player = player
        self.board = board
        self.rules = rules
        self.clickables = clickables
        
    def fase(self,control,event):
        if (not control.mill) and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, area in enumerate(self.clickables):
                    if area.collidepoint(event.pos):
                        if self.rules.casillaVacia(i, self.board.board):
                            self.rules.colocarPieza(i,self.player, self.board.board)
                            control.played = True
                            control.mill = self.rules.check_mill(i, self.board.board)
                            if not control.mill:
                                self.player=self.rules.changeTurn(self.player)
                                control.turn+=1
                            control.moveLoc = i
    
        
        