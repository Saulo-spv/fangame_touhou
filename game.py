import pygame
from player import Player

class Game:
    def __init__(self, screen):
        # Inicializa o jogo
        self.screen = screen
        self.clock = pygame.time.Clock()

        # Carrega o sprite sheet de Touhou
        sprite_sheet = pygame.image.load("images/sprite_sheet.png")

        # Grupos de sprites para todos os sprites e balas
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # Cria o jogador e adiciona ao grupo de todos os sprites
        self.player = Player(sprite_sheet, self.all_sprites, self.bullets)
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
            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)
            self.bullets.draw(self.screen)

            # Atualiza a tela
            pygame.display.flip()
            self.clock.tick(30)
