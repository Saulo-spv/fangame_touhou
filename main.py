import pygame
import sys

class Game():
    def __init__(self):
        pass
    
    def run(self):
        pass


if __name__ == '__main__':
    pygame.init()

    screen_width = 600
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))

    game = Game()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.run()

        pygame.display.flip()
        clock.tick(60)