import pygame
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, speed, degrees, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.midbottom = (pos[0]+10, pos[1]+10)

        self._speed = speed
        self._degrees = degrees

        self._dx = math.cos(math.radians(self._degrees)) * self._speed
        self._dy = -(math.sin(math.radians(self._degrees)) * self._speed)

    def move(self):
        # Movimenta o tiro
        self.rect.y -= self._dy
        self.rect.x += self._dx

    def screen_limit(self):
        # Remove o tiro quando atinge as bordas da tela
        if self.rect.bottom < 0 or self.rect.top > 600 or self.rect.left < 0 or self.rect.right > 800:
            self.kill()

    def update(self):
        self.move()
        self.screen_limit()


class PlayerBullet(Bullet):
    def __init__(self, pos):
        sprite_sheet = pygame.image.load("assets/images/player/sprite_sheet.png")
        image = sprite_sheet.subsurface(pygame.Rect(0, 150, 16, 16)).convert_alpha()

        # Inicializa e posiciona o tiro
        super().__init__(pos, 5, -90, image)


class EnemyBullet(Bullet):
    def __init__(self, pos, degrees, type):
        if type == 1:
            image = pygame.image.load('assets/images/enemies/bullet0.png')
        elif type == 2:
            image = pygame.image.load('assets/images/enemies/bullet1.png')
        elif type == 3:
            image = pygame.image.load('assets/images/enemies/bullet2.png')
        elif type == 4:
            image = pygame.image.load('assets/images/enemies/bullet2.png')

        super().__init__(pos, 2, degrees, image)