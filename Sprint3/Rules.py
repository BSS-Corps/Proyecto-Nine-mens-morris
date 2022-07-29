from Ficha import Ficha
from Tablero import Tablero
from Coordenadas import Coordenadas
import sys
sys.path.append(".")
#coord.coords.values()
coord = Coordenadas()
class Rules():

    def __init__(self):
        self.table = Tablero()

    def check_mill(self, idx, board):
        for i in range(2):
            if board[coord.mills[idx][i][0]]==board[idx] and board[coord.mills[idx][i][1]]==board[idx]:
                return True
        return False

    def casillaVacia(self, i, board):
        if(board[i] == 'x'):
            return True
        return False

    def changeTurn(self, player):
        if(player==0):
            player=1
        else:
            player=0
        return player

    def colocarPieza(self, i, player, board):

        if(player==0):
            board[i]='B'
        else:
            board[i]='W'

    def removerPieza(self, i, player, board):
        if player == 0:
            if board[i] == 'W':
                board[i] = 'x'
                return True
        elif player == 1:
            if board[i] == 'B':
                board[i] = 'x'
                return True
        return False
    # def check_mill(self, idx, board):
    #     for i in range(2):
    #         if self.board[self.mills[idx][i][0]]==self.board[idx] and self.board[self.mills[idx][i][1]]==board[idx]:
    #             return True
    #     return False

    # def casillaVacia(self, i,board):
    #     if(self.board[i] == 'x'):
    #         return True
    #     return False

    # def changeTurn(self):
    #     if(self.player==0):
    #         self.player=1
    #     else:
    #         player=0
    #     return player

    # def colocarPieza(self, i, board):
    #     if(self.player ==0):
    #         board[i]='B' 
    #     else:
    #         board[i]='W'

    # def removerPieza(self, i, board):
    #     if self.player == 0:
    #         if board[i] == 'W':
    #             board[i] = 'x'
    #             return True
    #     elif self.player == 1:
    #         if board[i] == 'B':
    #             board[i] = 'x'
    #             return True
    #     return False