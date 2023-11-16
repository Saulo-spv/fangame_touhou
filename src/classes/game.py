import pygame

from classes.player import Player
from classes.background import Background


class Game:
    def __init__(self):
        # Tamanho da tela
        self.screen_width = 800
        self.screen_height = 600

        # Inicializa o jogo
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()

        # Grupos de sprites para todos os sprites e balas
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # Cria o background e adiciona ao grupo de todos os sprites
        self.background = Background((800, 600), -7768, 5, 'assets/images/background/starfield.png')
        self.all_sprites.add(self.background)

        # Cria o jogador e adiciona ao grupo de todos os sprites
        player_sprite_sheet = pygame.image.load("assets/images/player/sprite_sheet.png")
        self.player = Player(player_sprite_sheet, self.all_sprites, self.bullets)
        self.all_sprites.add(self.player)

    def run(self):
        # Loop principal do jogo
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Atualiza os sprites
            self.all_sprites.update()
            self.bullets.update()

            # Desenha os sprites na tela
            self.all_sprites.draw(self.screen)
            self.bullets.draw(self.screen)

            # Atualiza a tela
            pygame.display.flip()
            self.clock.tick(31)
