import pygame

class GameOver():
    running = True

    def chekGameOver(self,event):
        if event.type == pygame.QUIT:
            self.running = False
        
