import pygame

from Oponent import Oponent

class FaseIntermedia():
    
    def __init__(self,player,board,rules,clickables):
        self.player = player
        self.board = board
        self.rules = rules
        self.clickables = clickables
    
    def fase(self,control,event):

        if (not control.played) and (not control.mill) and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                for i, area in enumerate(self.clickables):
                    if area.collidepoint(event.pos):
                        if (self.player.nro==0 and self.board.board[i]=='B') or (self.player.nro==1 and self.board.board[i]=='W'):
                            control.turn += 1
                            control.moveLoc = i
                            self.board.selectMove = True
        
        if self.board.selectMove and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, area in enumerate(self.clickables):
                    if area.collidepoint(event.pos):
                        if i in control.lugaresDisponibles:
                            self.rules.colocarPieza(i,self.player,self.board.board)
                            self.board.board[control.moveLoc] = 'x'
                            control.mill = self.rules.check_mill(i,self.board.board)
                            if not control.mill:
                                self.player=self.rules.changeTurn(self.player)
                                control.turn+=1
                            control.played = True
                            control.moveLoc = i
                            self.board.selectMove = False