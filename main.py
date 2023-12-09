import pygame
import sys

sys.path.append('./src')

from classes.game import Game


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()

    Game().main_menu()

    pygame.mixer.quit()
    pygame.quit()
    sys.exit()