import pygame
from tablero import mills

def casillaVacia(i,board):
    if(board[i] == 'x'):
        return True
    return False