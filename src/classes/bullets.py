"""Classe Bullet

Módulo responsável por implementar a classe Bullet, que representa um tiro do jogo.

"""

import pygame
import math

from classes.exceptions import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], speed: int, degrees: float, bullet_type: str):
        """Inicializa uma nova instância da classe Bullet.

        Parameters
        ----------
        pos : tuple[int, int]
            A posição inicial do tiro.
        speed : int
            A velocidade do tiro.
        degrees : float
            O ângulo de movimentação do tiro.
        bullet_type : str
            O tipo do tiro.
        """
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
        else:
            raise InvalidTypeException()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.midbottom = (pos[0]+10, pos[1]+10)

        self.__speed = speed
        self.__degrees = degrees

        self.__dx = math.cos(math.radians(self.__degrees)) * self.__speed
        self.__dy = -(math.sin(math.radians(self.__degrees)) * self.__speed)

    @property
    def hitbox(self) -> pygame.Rect:
        """Obtém a hitbox do tiro.

        Returns
        -------
        pygame.Rect
            A hitbox do tiro.
        """
        return self.__hitbox
    
    @hitbox.setter
    def hitbox(self, values: tuple[int, int, int, int]):
        """Define a hitbox do tiro.

        Parameters
        ----------
        values : tuple[int, int, int, int]
            Os valores da hitbox do tiro.
        """
        x, y, width, height = values
        self.__hitbox = pygame.Rect(x, y, width, height)

    def move(self):
        """Movimenta o tiro.
        """
        # Movimenta o tiro
        self.rect.y -= self.__dy
        self.rect.x += self.__dx

    def screen_limit(self):
        """Garante que o tiro não ultrapasse as bordas da tela.
        """
        # Remove o tiro quando atinge as bordas da tela
        if self.rect.bottom < 0 or self.rect.top > 600 or self.rect.left < 0 or self.rect.right > 800:
            self.kill()
    
    def update_hitbox(self):
        """Atualiza a hitbox do tiro.
        """
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
        """Atualiza o tiro.
        """
        self.move()
        self.screen_limit()
        self.update_hitbox()
