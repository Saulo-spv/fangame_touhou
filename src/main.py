import pygame
import sys

from classes.runner import Runner

if __name__ == '__main__':
    pygame.init()

    game = Runner()
    game.run()

    pygame.quit()
    sys.exit()