import pygame
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, speed, degrees, bullet_type):
        super().__init__()

        self.type = bullet_type

        if self.type == 'player':
            image = pygame.image.load("assets/images/player/sprite_sheet.png").subsurface(pygame.Rect(0, 150, 16, 16)).convert_alpha()
        elif self.type == 'enemy_1':
            image = pygame.image.load('assets/images/enemies/bullet0.png')
        elif self.type == 'enemy_2':
            image = pygame.image.load('assets/images/enemies/bullet1.png')
        elif self.type == 'enemy_3':
            image = pygame.image.load('assets/images/enemies/bullet2.png')
        elif self.type == 'enemy_4':
            image = pygame.image.load('assets/images/enemies/bullet3.png')

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.midbottom = (pos[0]+10, pos[1]+10)

        self._speed = speed
        self._degrees = degrees

        self._dx = math.cos(math.radians(self._degrees)) * self._speed
        self._dy = -(math.sin(math.radians(self._degrees)) * self._speed)

    @property
    def hitbox(self):
        return self.__hitbox
    
    @hitbox.setter
    def hitbox(self, values):
        x, y, width, height = values
        self.__hitbox = pygame.Rect(x, y, width, height)

    def move(self):
        # Movimenta o tiro
        self.rect.y -= self._dy
        self.rect.x += self._dx

    def screen_limit(self):
        # Remove o tiro quando atinge as bordas da tela
        if self.rect.bottom < 0 or self.rect.top > 600 or self.rect.left < 0 or self.rect.right > 800:
            self.kill()
    
    def update_hitbox(self):
        if self.type == 'player':
            self.hitbox = (self.rect.centerx-5, self.rect.centery-5, 15, 15)
        elif self.type == 'enemy_1':
            self.hitbox = (self.rect.centerx-10, self.rect.centery-10, 20, 20)
        elif self.type == 'enemy_2':
            self.hitbox = (self.rect.centerx-15, self.rect.centery-15, 30, 30)
        elif self.type == 'enemy_3':
            self.hitbox = (self.rect.centerx-8, self.rect.centery-8, 17, 17)
        elif self.type == 'enemy_4':
            self.hitbox = (self.rect.centerx-5, self.rect.centery-5, 10, 10)

    def update(self):
        self.move()
        self.screen_limit()
        self.update_hitbox()
