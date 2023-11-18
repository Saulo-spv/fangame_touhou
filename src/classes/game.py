import pygame

class Game:
    screen_width = 800
    screen_height = 600
    clock_tick = 30
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()