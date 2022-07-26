import pygame
from Tablero import Tablero

pygame.init()
screen = pygame.display.set_mode((500, 630))
running = True
pygame.display.set_caption("Nine Men's Morris")
board = Tablero()

while running:
    screen.fill((255, 255, 255))
    screen.blit(board.boardImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    board.drawBoard(screen)

    pygame.display.update()