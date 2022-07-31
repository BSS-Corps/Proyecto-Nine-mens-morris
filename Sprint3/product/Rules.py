from Ficha import Ficha
from Tablero import Tablero
from Coordenadas import Coordenadas
import sys
sys.path.append(".")
#coord.coords.values()
coord = Coordenadas()
class Rules():

    # def __init__(self):
    #     self.table = Tablero()

    def check_mill(self, idx, board):
        for i in range(2):
            if (board[coord.mills[idx][i][0]]==board[idx]) and (board[coord.mills[idx][i][1]]==board[idx]):
                return True
        return False

    def casillaVacia(self, i, board):
        if(board[i] == 'x'):
            return True
        return False

    def changeTurn(self, player):
        if(player.nro==0):
            player.nro=1
            player.simb = "W"
        else:
            player.nro=0
            player.simb = "B"
        return player

    def colocarPieza(self, i, player, board):
        #board[i] = player.simb
        if(player.nro==0):
           board[i]='B'
        else:
           board[i]='W'

    def removerPieza(self, i, player, board):
        if player.nro == 0:
            if board[i] == 'W':
                board[i] = 'x'
                return True
        elif player.nro == 1:
            if board[i] == 'B':
                board[i] = 'x'
                return True
        return False

    def checkEndgame(self, player,board):
        cnt = 0
        if(player.nro==0):
            for b in board:
                if b == 'B':
                    cnt += 1
            if cnt == 3:
                return True
        elif(player.nro==1):
            for b in board:
                if b == 'W':
                    cnt += 1
            if cnt == 3:
                return True
        return False


    def checkGameComplete(self,control,board):
            cnt1, cnt2 = 0, 0
            for b in board:
                if b == 'B':
                    cnt1 += 1
                if b == 'W':
                    cnt2 += 1
            if cnt2 < 3:
                return 1
            if cnt1 < 3:
                return 2
            return 0
