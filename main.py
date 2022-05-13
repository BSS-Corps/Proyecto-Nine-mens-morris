from turtle import Screen
import pygame, sys
import tablero

board = tablero.Tablero()
board.draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()