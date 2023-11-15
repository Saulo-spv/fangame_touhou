import pygame
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        # Carregando o sprite sheet de Touhou
        sprite_sheet = pygame.image.load("images/sprite_sheet.png")

        # Criação de sprites
        player_sprite_coordinates = (0, 0, 32, 50)
        sprite_width = 32
        sprite_height = 46
        screen_height = screen.get_height()
        screen_width = screen.get_width()

        self.player = Player(sprite_sheet, *player_sprite_coordinates, sprite_width, sprite_height, screen_height, screen_width)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.all_sprites.update(keys)

            # Desenha os sprites
            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)