class Coordenada:

    def init(self,x,y):
        self.x = x
        self.y = y
        self.estado = 0

    def cambio_estado(self,estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def get_coordenada(self):
        a = (self.x,self.y)
        return a