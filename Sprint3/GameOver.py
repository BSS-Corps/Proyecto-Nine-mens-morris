import pygame
import sys

class GameOver():
    running = True

    def chekGameOver(self,event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #self.running = False
        
