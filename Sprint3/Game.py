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
screen = pygame.display.set_mode((500, 630))
#turnosdisponibles = []
#lugaresDisponibles = []
#turn = 0
pygame.display.set_caption("Nine Men's Morris")
board = Tablero()
coord = Coordenadas()
rules = Rules()
game = GameOver()
#mill = False
#mul = 500/843
#board.mul = mul
clickables = [pygame.Rect(MUL*c[0], MUL*c[1], 35, 35) for c in coord.coords.values()]
#clickables = [pygame.Rect(mul*c[0], mul*c[1], 35, 35) for c in coords.values()]
#player = 0
#played = False
player = Player(0,"W")
control = Controlador()
fase1 = FaseTemprana(player,board,rules,clickables)
fase2 = FaseTemprana(player,board,rules,clickables)
mill = Mill()

while game.running:
    screen.fill((255, 255, 255))
    screen.blit(board.boardImg, (0, 0))
    # endGame1 = board.checkEndgame(0)
    # endGame2 = board.checkEndgame(1)
    for event in pygame.event.get():
        game.chekGameOver(event)
        #if event.type == pygame.QUIT:
        #    running = False
        
        if control.turn<18 and control.fase == 1:
            fase1.fase(control,event)
            mill.aMill(control,event,fase1)
            
        # earlyGame --> midGame
        if control.turn == 18 and control.fase ==1:
            control.changephase()
            print(f"PASANDO DE FASE {control.fase-1} a {control.fase}")
            fase2aux = FaseIntermedia(fase1.player,fase1.board,fase1.rules,fase1.clickables)
            fase2 = fase2aux
        
        if control.turn>=18 and control.fase == 2:
            fase2.fase(control,event)
            mill.aMill(control,event,fase2)
            

        # if (not mill) and turn< 18 and event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         for i, area in enumerate(clickables):
        #             if area.collidepoint(event.pos):
        #                 if rules.casillaVacia(i, board.board):
        #                     rules.colocarPieza(i,player.type, board.board)
        #                     played = True
        #                     mill = rules.check_mill(i, board.board)
        #                     if not mill:
        #                         player=rules.changeTurn(player)
        #                         turn+=1
        #                     moveLoc = i

        # mill
        # if mill and event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button ==1:
        #         for i, area in enumerate(clickables):
        #             if area.collidepoint(event.pos):
        #                 mill=not rules.removerPieza(i,player,board.board)
        #                 if not mill:
        #                     player = rules.changeTurn(player)
        #                     turn+=1
        #                     moveLoc=None

		# # midgame
        # if board.selectMove and turn > 18 and event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         for i, area in enumerate(clickables):
        #             if area.collidepoint(event.pos):
        #                 if i in control.lugaresDisponibles:
        #                     rules.colocarPieza(i,player,board.board)
        #                     board.board[moveLoc] = 'x'
        #                     mill = rules.check_mill(i,board.board)
        #                     if not mill:
        #                         player=rules.changeTurn(player)
        #                         turn+=1
        #                     played = True
        #                     moveLoc = i
        #                     board.selectMove = False


		# also midgame
		#Selecciona la pieza a mover o volar
        # if (not played) and (not mill) and turn >= 18 and event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1: 
        #         for i, area in enumerate(clickables):
        #             if area.collidepoint(event.pos):
        #                 if (player==0 and board.board[i]=='B') or (player==1 and board.board[i]=='W'):
        #                     turn += 1
        #                     moveLoc = i
        #                     board.selectMove = True

		# restart logic
        if control.gameComplete != 0:
			#screen.blit(openingText, text_rect)
            print(f'Gano jugador{control.gameComplete}')
            control.gameComplete = False
            control.played = False
            board = Tablero()
            fase1 = FaseTemprana(player,board,rules,clickables)
            fase2 = FaseTemprana(player,board,rules,clickables)
            control.moveLoc = None
            control.turn = 0

    fase2.board.drawBoard(screen,control,player)
    #print(board.drawBoard(screen))

    pygame.display.update()
    control.played=False