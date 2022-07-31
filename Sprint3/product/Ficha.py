import pygame
import os

class Ficha:
    sourceFileDir = os.path.dirname(os.path.abspath(__file__))
    f2 = os.path.join(sourceFileDir, '../../static/black.png')
    f3 = os.path.join(sourceFileDir, '../../static/white.png')
    f4 = os.path.join(sourceFileDir, '../../static/high.png')
    def __init__(self):
        self.blackImg = pygame.image.load(self.f2)
        self.whiteImg = pygame.image.load(self.f3)
        self.highImg = pygame.image.load(self.f4)