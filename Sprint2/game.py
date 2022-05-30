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
	for loc in range(len(board)):
		if board[loc] == 'W':
			x = mul*coords[loc][0]
			y = mul*coords[loc][1]
			screen.blit(whiteImg,(x, y))
		if board[loc] == 'B':
			x = mul*coords[loc][0]
			y = mul*coords[loc][1]
			screen.blit(blackImg,(x, y))


while running:
	screen.fill((255, 255, 255))
	screen.blit(boardImg, (0, 0))
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			running = False


	
		if (not mill) and turn < 18 and event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:  # Left mouse button.
					# Check if the rect collides with the mouse pos.
				for i, area in enumerate(clickables):
					if area.collidepoint(event.pos):
						if casillaVacia(i,board):
							if(player==0):
								board[i]='B'
								player=1
							else:
								board[i]='W'
								player=0 
							played = True
							turn+=1
						else:
							played = False
						#moveLoc = i
						#print(mill)
		

	
	drawBoard()
	
	pygame.display.update()
