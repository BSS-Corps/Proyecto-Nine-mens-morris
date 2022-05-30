import pygame
from tablero import mills

def casillaVacia(i,board):
    if(board[i] == 'x'):
        return True
    return False

def changeTurn(player):
    if(player==0):
        player=1
    else:
        player=0
    return player

def colocarPieza(i, player, board):
    if(player==0):
        board[i]='B' 
    else:
        board[i]='W'
