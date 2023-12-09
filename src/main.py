import pygame
import sys
from classes.game import Game
from classes.menu import Menu

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()

    menu = Menu()
    menu.run_menu()


    game = Game()
    game.run()

    pygame.mixer.quit()
    pygame.quit()
    sys.exit()