import pygame

from classes.game import Game
from classes.player import Player
from classes.background import Background
from classes.enemies import *

class Runner:
    def __init__(self):
        # Inicializa o jogo
        self.screen = pygame.display.set_mode((Game.screen_width, Game.screen_height))
        self.clock = pygame.time.Clock()

        # Cria o background e adiciona ao grupo de todos os sprites
        self.background = Background((800, 600), -7768, 1, 'assets/images/background/starfield.png')
        Game.all_sprites.add(self.background)

        # Cria o jogador e adiciona ao grupo de todos os sprites
        self.player = Player()
        Game.all_sprites.add(self.player)

        Game.all_sprites.add([
            BigFairyType1(),
            BigFairyType2(),
            BigFairyType3(),
            SmallFairy(1),
            SmallFairy(2)
        ])

    def run(self):
        # Loop principal do jogo
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Atualiza os sprites
            Game.all_sprites.update()

            # Desenha os sprites na tela
            Game.all_sprites.draw(self.screen)

            # Atualiza a tela
            pygame.display.flip()
            self.clock.tick(Game.clock_tick)
