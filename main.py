import pygame
import sys
from game import Game

if __name__ == '__main__':
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    game = Game(screen)
    game.run()

    pygame.quit()
    sys.exit()