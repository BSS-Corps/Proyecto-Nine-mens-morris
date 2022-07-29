

class Controlador():
    
    def __init__(self):
        self.turn = 0
        self.played = False
        self.mill = False
        self.fase = 1
        self.moveLoc = None
        self.lugaresDisponibles = []
        self.endGame1 =  False
        self.endGame2 = False
        self.gameComplete = 0
    
    def changephase(self):
        self.fase+=1
