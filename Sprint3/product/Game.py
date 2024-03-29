from msvcrt import open_osfhandle
from Oponent import Oponent
from constants import MUL, turn
import pygame
from Coordenadas import Coordenadas
from Tablero import Tablero
from Rules import Rules
from GameOver import GameOver
from Player import Player
from Controlador import Controlador
from FaseTemprana import FaseTemprana
from FaseIntermedia import FaseIntermedia
from MIll import Mill

pygame.init()
Font = pygame.font.SysFont('Roboto Mono',40)

win1Text=Font.render("Gana Jugador 1",False,(0,255,0))
win2Text=Font.render("Gana Jugador 2",False,(0,0,255))
win3Text=Font.render("Gana Computadora",False,(255,0,0))
winText=Font.render("Ganaste!",False,(0,125,255))
# result=

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 630))
        pygame.display.set_caption("Nine Men's Morris")

        self.board = Tablero()
        self.coord = Coordenadas()
        self.rules = Rules()
        self.game = GameOver()

        self.clickables = [
            pygame.Rect(MUL * c[0], MUL * c[1], 35, 35)
            for c in self.coord.coords.values()
        ]

        self.player = Player(0, "W")
        self.control = Controlador()
        self.fase1 = FaseTemprana(self.player, self.board, self.rules,
                                  self.clickables)
        self.fase2 = FaseTemprana(self.player, self.board, self.rules,
                                  self.clickables)
        self.mill = Mill()

        self.clock = pygame.time.Clock()

    def oponente_virtual(self):
        screen = self.screen
        board = self.board
        rules = self.rules
        game = self.game
        player = self.player
        control = self.control
        fase1 = self.fase1
        fase2 = self.fase2
        mill = self.mill
        clock = self.clock
        clickables = self.clickables

        while game.running:
            screen.fill((255, 255, 255))
            screen.blit(board.boardImg, (0, 0))
            # endGame1 = board.checkEndgame(0)
            # endGame2 = board.checkEndgame(1)
            for event in pygame.event.get():
                game.chekGameOver(event)
                #if event.type == pygame.QUIT:
                #    running = False

                if control.turn < 18 and control.fase == 1 and fase1.player.nro == 0:
                    fase1.fase(control, event)
                    mill.aMill(control, event, fase1)

                # earlyGame --> midGame
                if control.turn == 18 and control.fase == 1:
                    control.changephase()
                    print(f"PASANDO DE FASE {control.fase-1} a {control.fase}")
                    fase2 = FaseIntermedia(fase1.player, fase1.board,
                                           fase1.rules, fase1.clickables)

                if control.turn >= 18 and control.fase == 2 and fase2.player.nro == 0:
                    fase2.fase(control, event)
                    mill.aMill(control, event, fase2)
                    if fase2.player.nro == 0:
                        control.endGame1 = fase2.rules.checkEndgame(
                            fase2.player, fase2.board.board)
                    # control.endGame2 = fase.rules.checkEndgame(fase.player,fase.board.board)
                    control.gameComplete = fase2.rules.checkGameComplete(
                        control, fase2.board.board)

                if control.gameComplete != 0:
                    #screen.blit(openingText, text_rect)
                    # print(f'Gano jugador{control.gameComplete}')
                    # control.gameComplete = False
                    control.played = False
                    # board = Tablero()
                    fase1 = FaseTemprana(player, board, rules, clickables)
                    fase2 = FaseTemprana(player, board, rules, clickables)
                    control.moveLoc = None
                    control.turn = 0

            fase2.board.drawBoard(screen, control, player)
            if control.gameComplete==1:
                screen.blit(winText,(50,550))
            if control.gameComplete==2:
                screen.blit(win3Text,(50,550))
            pygame.display.update()
            clock.tick(20)
            
            if control.turn <= 18 and (not control.mill) and control.played:
                oponente = Oponent()
                newBoard=oponente.selectInitOpMov(fase1.board.board)
                fase1.board.board = newBoard.copy()
                fase1.player = rules.changeTurn(fase1.player)
                control.turn += 1
                control.played = False
                fase1.board.selectMove = False

            if control.turn >= 18 and (not control.mill) and (
                    not fase2.board.selectMove) and control.played:
                oponente = Oponent()
                newBoard=oponente.selectOpMov(fase2.board.board)
                fase2.board.board = newBoard.copy()
                fase2.player = rules.changeTurn(fase2.player)
                control.turn += 1
                control.moveLoc=None
                fase2.board.selectMove=False
                control.mill = False
                control.played = False

            fase2.board.drawBoard(screen, control, player)
            pygame.display.update()
            clock.tick(20)

    def oponente_real(self):
        screen = self.screen
        board = self.board
        coord = self.coord
        rules = self.rules
        game = self.game
        player = self.player
        control = self.control
        fase1 = self.fase1
        fase2 = self.fase2
        mill = self.mill
        clock = self.clock
        clickables = self.clickables

        while game.running:
            screen.fill((255, 255, 255))
            screen.blit(board.boardImg, (0, 0))
            # endGame1 = board.checkEndgame(0)
            # endGame2 = board.checkEndgame(1)
            for event in pygame.event.get():
                game.chekGameOver(event)
                #if event.type == pygame.QUIT:
                #    running = False

                if control.turn < 18 and control.fase == 1:
                    fase1.fase(control, event)
                    mill.aMill(control, event, fase1)

                # earlyGame --> midGame
                if control.turn == 18 and control.fase == 1:
                    control.changephase()
                    print(f"PASANDO DE FASE {control.fase-1} a {control.fase}")
                    fase2aux = FaseIntermedia(fase1.player, fase1.board,
                                              fase1.rules, fase1.clickables)
                    fase2 = fase2aux

                if control.turn >= 18 and control.fase == 2:
                    fase2.fase(control, event)
                    mill.aMill(control, event, fase2)
                    if fase2.player.nro == 0:
                        control.endGame1 = fase2.rules.checkEndgame(
                            fase2.player, fase2.board.board)
                    else:
                        control.endGame2 = fase2.rules.checkEndgame(
                            fase2.player, fase2.board.board)
                    control.gameComplete = fase2.rules.checkGameComplete(
                        control, fase2.board.board)

                # restart logic
                if control.gameComplete != 0:
                    #screen.blit(openingText, text_rect)
                    # print(f'Gano jugador{control.gameComplete}')

                    # control.gameComplete = False
                    control.played = False
                    # board = Tablero()
                    fase1 = FaseTemprana(player, board, rules, clickables)
                    fase2 = FaseTemprana(player, board, rules, clickables)
                    control.moveLoc = None
                    control.turn = 0

            fase2.board.drawBoard(screen, control, player)
            if control.gameComplete==1:
                screen.blit(win1Text,(50,550))
            if control.gameComplete==2:
                screen.blit(win2Text,(50,550))
            pygame.display.update()
            control.played = False