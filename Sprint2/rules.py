import pygame
import sys
sys.path.append(".")
#from product import *
from tablero import mills


def check_mill(idx, board):
    for i in range(2):
        if board[mills[idx][i][0]]==board[idx] and board[mills[idx][i][1]]==board[idx]:
            return True
    return False

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
