from Coordenadas import Coordenadas

class Oponent():
    def __init__(self):
        self.level = 5
        self.selectedMove = None

    def nposibleMills(self, board):
        #Mills
        nBMills = 0
        nWMills = 0
        #Posibles Mills
        npBMills = 0
        npWMills = 0

        n_board = len(board)

        for i in range(n_board):
            if board[i] == 'W':
                if self.isMill(i, board):
                    nWMills += 1
                if self.posibleMill(i, board):
                    npWMills += 1
            if board[i] == 'B':
                if self.isMill(i, board):
                    nBMills += 1
                if self.posibleMill(i, board):
                    npBMills += 1

        return nWMills, nBMills, npWMills, npBMills

    def posibleMill(self, pos, board):
        for vec in Coordenadas().mills[pos]:
            if (board[vec[0]] == board[pos]) and (board[vec[1]] == "x"):
                return True
            if (board[vec[0]] == "x") and (board[vec[1]] == board[pos]):
                return True
        return False

    def faseTempranaTurn(self, board):
        #Numero de Piezas
        w = 0
        b = 0
        for pieza in board:
            if pieza == "W":
                w += 1
            if pieza == "B":
                b += 1
        nWM, nBM, npWMills, npBMills = self.nposibleMills(board)

        return 100 * ((w - b) + 3 * (nWM - nBM) + 2 * (npWMills - npBMills))

    def faseIntermediaTurn(self, board):
        #Numero de Piezas
        w = 0
        b = 0
        for pieza in board:
            if pieza == "W":
                w += 1
            if pieza == "B":
                b += 1
        #Posibles movimientos oponente
        n_b = len(self.movs_faseIntermedia(board, "B"))

        nWM, nBM, npWMills, npBMills = self.nposibleMills(board)

        #Puntajes de Victoria
        if b <= 2:
            return 10000
        elif n_b == 0:
            return 10000
        #Puntaje de Derrota
        elif w <= 2:
            return -10000
        #Puntaje segun piezas restantes, Mills formados y posibles
        else:
            return 100 * ((w - b) + 3 * (nWM - nBM) + 2 *
                          (npWMills - npBMills)) - n_b

    def movs_faseIntermedia(self, board, color):
        b = 0
        for pieza in board:
            if pieza == color:
                b += 1

        if b == 3:
            #Fase Final(puede volar)
            movs = self.movs_flying(board, color)
        else:
            movs = self.movs_normal(board, color)

        return movs

    def movs_normal(self, board, color):
        movs = []
        n_board = len(board)
        for i in range(n_board):
            if board[i] == color:
                ady = Coordenadas().neighbors[i]
                for a in ady:
                    if board[a] == "x":
                        new_board = board.copy()
                        new_board[i] = "x"
                        new_board[a] = color
                        if self.isMill(a, new_board):
                            self.eliminar(new_board, movs, color)
                        else:
                            movs.append(new_board)
        return movs

    def movs_flying(self, board, color):
        movs = []
        n_board = len(board)
        for i in range(n_board):
            if board[i] == color:
                for j in range(n_board):
                    #A cualquier espacio libre
                    if board[j] == 'x':
                        new_board = board.copy()
                        new_board[i] = 'x'
                        new_board[j] = color
                        if self.isMill(j, new_board):
                            self.eliminar(new_board, movs, color)
                        else:
                            movs.append(new_board)
        return movs

    def isMill(self, pos, board):
        for vec in Coordenadas().mills[pos]:
            if (board[vec[0]] == board[pos]) and (board[vec[1]] == board[pos]):
                return True
        return False

    def eliminar(self, board, mov, color):
        elim_color = "B"
        if color == "B":
            elim_color = "W"
        n = 0
        n_board = len(board)
        for i in range(n_board):
            if board[i] == elim_color:
                if not self.isMill(i, board):
                    new_board = board.copy()
                    new_board[i] = "x"
                    mov.append(new_board)
                    n += 1
        if n == 0:
            mov.append(board.copy())

    def selectOpMov(self,board):
        v=-100000
        mov=None
        posibles=self.movs_faseIntermedia(board,"W")
        for p in posibles:
            new_v=self.faseIntermediaTurn(p)
            if new_v>v:
                v=new_v
                mov=p.copy()
        return mov

    def selectInitOpMov(self,board):
        v=-100000
        mov=None
        posibles=self.movs_faseTemprana(board,"W")
        for p in posibles:
            new_v=self.faseTempranaTurn(p)
            if new_v>v:
                v=new_v
                mov=p.copy()
        return mov

    def movs_faseTemprana(self,board,color):
        movs=[]
        n_board=len(board)
        for i in range(n_board):
            if board[i]=="x":
                new_board=board.copy()
                new_board[i]=color
                if self.isMill(i,new_board):
                    self.eliminar(new_board,movs,color)
                else:
                    movs.append(new_board)
        return movs
