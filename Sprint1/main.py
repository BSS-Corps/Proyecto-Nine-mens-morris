import pygame
from game import *
import os
from time import sleep

def main():
    pygame.init()

    pygame.display.set_caption("Nine Men's Morris")


    fps = 20
    clock = pygame.time.Clock()

    clock.tick(fps)

if __name__ == "__main__":
    main()