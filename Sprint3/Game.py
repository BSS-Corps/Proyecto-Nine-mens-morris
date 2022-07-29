from constants import MUL, player, turn
import pygame
from Coordenadas import Coordenadas
from Tablero import Tablero
from Rules import Rules

pygame.init()
screen = pygame.display.set_mode((500, 630))
turnosdisponibles = []
running = True
lugaresDisponibles = []
#turn = 0
pygame.display.set_caption("Nine Men's Morris")
board = Tablero()
coord = Coordenadas()
rules = Rules()
mill = False
#mul = 500/843
#board.mul = mul
clickables = [pygame.Rect(MUL*c[0], MUL*c[1], 35, 35) for c in coord.coords.values()]
#clickables = [pygame.Rect(mul*c[0], mul*c[1], 35, 35) for c in coords.values()]
#player = 0
played = False


while running:
    screen.fill((255, 255, 255))
    screen.blit(board.boardImg, (0, 0))
    endGame1 = board.checkEndgame(0)
    endGame2 = board.checkEndgame(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (not mill) and turn< 18 and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, area in enumerate(clickables):
                    if area.collidepoint(event.pos):
                        if rules.casillaVacia(i, board.board):
                            rules.colocarPieza(i,player, board.board)
                            played = True
                            mill = rules.check_mill(i, board.board)
                            if not mill:
                                player=rules.changeTurn(player)
                                turn+=1
                            moveLoc = i

        # mill
        if mill and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button ==1:
                for i, area in enumerate(clickables):
                    if area.collidepoint(event.pos):
                        mill=not rules.removerPieza(i,player,board.board)
                        if not mill:
                            player = rules.changeTurn(player)
                            turn+=1
                            moveLoc=None

		# # midgame
        if board.selectMove and turn > 18 and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, area in enumerate(clickables):
                    if area.collidepoint(event.pos):
                        if i in lugaresDisponibles:
                            rules.colocarPieza(i,player,board.board)
                            board[moveLoc] = 'x'
                            mill = rules.check_mill(i,board.board)
                            if not mill:
                                player=rules.changeTurn(player)
                                turn+=1
                            played = True
                            moveLoc = i
                            board.selectMove = False


		# also midgame
		#Selecciona la pieza a mover o volar
        if (not played) and (not mill) and turn >= 18 and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                for i, area in enumerate(clickables):
                    if area.collidepoint(event.pos):
                        if (player==0 and board.board[i]=='B') or (player==1 and board.board[i]=='W'):
                            turn += 1
                            moveLoc = i
                            board.selectMove = True

		# restart logic
        #if gameComplete != 0:
			#screen.blit(openingText, text_rect)
            print(f'Gano jugador{board.gameComplete}')
            board.gameComplete = False
            played = False
            board.board = list('xxxxxxxxxxxxxxxxxxxxxxxx')
            moveLoc = None
            turn = 0

    board.drawBoard(screen)
    print(board.drawBoard(screen))

    pygame.display.update()
    played=False