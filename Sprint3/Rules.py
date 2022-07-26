from Tablero import mills

class Rules:
    def __init__(self,player):
        self.player = player

    def check_mill(self, idx, board):
        for i in range(2):
            if board[mills[idx][i][0]]==board[idx] and board[mills[idx][i][1]]==board[idx]:
                return True
        return False

    def casillaVacia(self, i,board):
        if(board[i] == 'x'):
            return True
        return False

    def changeTurn(self, player):
        if(self.player==0):
            self.player=1
        else:
            player=0
        return player

    def colocarPieza(i, player, board):
        if(player==0):
            board[i]='B' 
        else:
            board[i]='W'

    def removerPieza(i, player, board):
        if player == 0:
            if board[i] == 'W':
                board[i] = 'x'
                return True
        elif player == 1:
            if board[i] == 'B':
                board[i] = 'x'
                return True
        return False