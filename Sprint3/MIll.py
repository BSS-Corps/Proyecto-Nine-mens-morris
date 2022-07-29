import pygame

class Mill():

    def aMill(self,control,event,fase):
        if control.mill and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button ==1:
                    for i, area in enumerate(fase.clickables):
                        if area.collidepoint(event.pos):
                            control.mill=not fase.rules.removerPieza(i,fase.player,fase.board.board)
                            if not control.mill:
                                fase.player = fase.rules.changeTurn(fase.player)
                                control.turn+=1
                                control.moveLoc=None
                                if control.turn > 18:
                                    if fase.player.nro == 0:
                                        control.endGame1 = fase.rules.checkEndgame(fase.player,fase.board.board)
                                    control.endGame2 = fase.rules.checkEndgame(fase.player,fase.board.board)
                                    control.gameComplete = fase.rules.checkGameComplete(control,fase.board.board)