import pygame
from ficha import *
from tablero import *
from rules import *

blackImg = pygame.image.load(f2)
whiteImg = pygame.image.load(f3)
highImg = pygame.image.load(f4)

turnosdisponibles = []

screen = pygame.display.set_mode((500, 630))
gameComplete = 0
turn = 0
player = 0
mul = 500/843
mill = False
v = 0
played = False
moveLoc = None
running = True
endGame = False
selectMove = False

MAX = 50000

clickables = [pygame.Rect(mul*c[0], mul*c[1], 35, 35) for c in coords.values()]
board = list('xxxxxxxxxxxxxxxxxxxxxxxx')

endGame1 = False
endGame2 = False

def checkEndgame(player):
	global endGame
	endGame = False
	cnt = 0
	if(player==0):
		for b in board:
			if b == 'B':
				cnt += 1
		if cnt == 3:
			return True
	elif(player==1):
		for b in board:
			if b == 'W':
				cnt += 1
		if cnt == 3:
			return True
	return False

def checkGameComplete():
	global gameComplete

	if turn > 18:
		cnt1, cnt2 = 0, 0
		for b in board:
			if b == 'B':
				cnt1 += 1
			if b == 'W':
				cnt2 += 1
		if cnt2 < 3:
			gameComplete = 1
		if cnt1 < 3:
			gameComplete = 2


def drawBoard():
	global lugaresDisponibles, mill, moveLoc
	# midgame

	if selectMove:
		if endGame1 and player==0:
			lugaresDisponibles = []
			for loc in range(len(board)):
				if board[loc] == 'x':
					lugaresDisponibles.append(loc)
					x = mul*coords[loc][0]
					y = mul*coords[loc][1]
					screen.blit(highImg,(x, y))
		elif endGame2 and player==1:
			lugaresDisponibles = []
			for loc in range(len(board)):
				if board[loc] == 'x':
					lugaresDisponibles.append(loc)
					x = mul*coords[loc][0]
					y = mul*coords[loc][1]
					screen.blit(highImg,(x, y))
		else:
			n = neighbors[moveLoc]
			lugaresDisponibles = []
			for j in n:
				if board[j] == 'x':
					lugaresDisponibles.append(j)
					x = mul*coords[j][0]
					y = mul*coords[j][1]
					screen.blit(highImg,(x, y))


	# dibuja las piezas
	for loc in range(len(board)):
			if board[loc] == 'W':
				x = mul*coords[loc][0]
				y = mul*coords[loc][1]
				screen.blit(whiteImg,(x, y))
			if board[loc] == 'B':
				x = mul*coords[loc][0]
				y = mul*coords[loc][1]
				screen.blit(blackImg,(x, y))
