"""Classe Enemy

Módulo responsável por implementar a classe Enemy, que representa um inimigo do jogo.

"""
import pygame
import random
from abc import ABC, abstractmethod

from classes.bullets import *
from classes.entity import Entity


class Enemy(Entity, ABC):
    def __init__(self, life: int, shoot_cooldown: int):
        """Inicializa uma nova instância da classe Enemy.

        Parameters
        ----------
        life : int
            A quantidade inicial de vida do inimigo.
        shoot_cooldown : int
            O tempo de espera entre disparos.
        """
        super().__init__(life, shoot_cooldown)

    @abstractmethod
    def move(self):
        """Move o inimigo.
        """
        pass

    @abstractmethod
    def update_animation(self):
        """Atualiza a animação do inimigo.
        """
        pass

    @abstractmethod
    def update_hitbox(self):
        """Atualiza a hitbox do inimigo.
        """
        pass

    @abstractmethod
    def recharge(self):
        """Obtém as balas disparadas pelo inimigo.
        """
        pass

    def screen_limit(self):
        """Verifica se o inimigo saiu da tela.
        """
        if self.rect.top >= 600:
            self.kill()
    
    def drop_power_up(self):
        """
        """
        if random.randint(0, 100) <= 20:
            power_up = random.choice(['life', 'shield', 'clear_bullets'])
            return power_up


class BigFairy(Enemy):
    def __init__(self, enemy_type):
        """Inicializa uma nova instância da classe BigFairy.

        Parameters
        ----------
        enemy_type : int
            O tipo do inimigo.
        """
        self.type = enemy_type

        self.__sprites = [pygame.image.load(f"assets/images/enemies/fairy{self.type}_{i}.png") for i in range(4)]
        self.__sprites_turn = [pygame.image.load(f"assets/images/enemies/turn{self.type}_{i}.png") for i in range(4)]

        self.image = self.__sprites[0]

        # Configurações de animação
        self.__animation_count = 0
        self.__last_frame_time = 0
        self.__animation_cooldown = 70
        
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.x = random.randint(20, 780)

        # Configurações de velocidade
        self.__x_speed = random.uniform(-2, 2)
        self.__y_speed = random.uniform(1.7, 1.8)
        self.__stay_y = random.randint(100, 300)

        self.__bullet_direction = 0

        if self.type == 3:
            shoot_cooldown = 400
        else:
            shoot_cooldown = 1500

        super().__init__(10, shoot_cooldown)

    def update_animation(self):
        """Atualiza a animação do inimigo.
        """
        current_time = pygame.time.get_ticks()

        if self.__x_speed == 0:
            if current_time - self.__last_frame_time > self.__animation_cooldown:
                self.__last_frame_time = pygame.time.get_ticks()
                self.__animation_count += 1

                if self.__animation_count >= len(self.__sprites):
                    self.__animation_count = 0

                self.image = self.__sprites[self.__animation_count]
        elif self.__x_speed < 0:
            if current_time - self.__last_frame_time > self.__animation_cooldown:
                self.__last_frame_time = pygame.time.get_ticks()
                self.__animation_count += 1

                if self.__animation_count >= len(self.__sprites_turn):
                    self.__animation_count = 0

                flipped_turn = pygame.transform.flip(self.__sprites_turn[self.__animation_count], True, False)

                self.image = flipped_turn
        elif self.__x_speed > 0:
            if current_time - self.__last_frame_time > self.__animation_cooldown:
                self.__last_frame_time = pygame.time.get_ticks()
                self.__animation_count += 1

                if self.__animation_count >= len(self.__sprites_turn):
                    self.__animation_count = 0

                self.image = self.__sprites_turn[self.__animation_count]

    def move(self):
        """Move o inimigo.
        """
        # Faz o inimigo parar em uma certa altura
        if self.rect.y >= self.__stay_y:
            self.__x_speed = 0
            self.__y_speed = 0
        else:
            self.rect.x += self.__x_speed
            self.rect.y += self.__y_speed

            if self.rect.left <= 0 or self.rect.right >= 800:
                self.__x_speed *= -1
    
    def update_hitbox(self):
        """Atualiza a hitbox do inimigo.
        """
        self.hitbox = (self.rect.x, self.rect.y, 50, 50)
    
    def recharge(self) -> pygame.sprite.Group:
        """Obtém as balas disparadas pelo inimigo.

        Returns
        -------
        pygame.sprite.Group
            O grupo de sprites com os novos tiros.
        """
        if self.type == 1:
            bullets = [
                Bullet((self.rect.centerx, self.rect.centery), 2, 0, 'enemy_1'),
                Bullet((self.rect.centerx, self.rect.centery), 2, 90, 'enemy_1'),
                Bullet((self.rect.centerx, self.rect.centery), 2, 180, 'enemy_1'),
                Bullet((self.rect.centerx, self.rect.centery), 2, 270, 'enemy_1'),
            ]
        elif self.type == 2:
            bullets = [
                Bullet((self.rect.centerx, self.rect.top + 10), 2, 30, 'enemy_2'),
                Bullet((self.rect.centerx, self.rect.top + 10), 2, 60, 'enemy_2'),
                Bullet((self.rect.centerx, self.rect.top + 10), 2, 90, 'enemy_2'),
                Bullet((self.rect.centerx, self.rect.top + 10), 2, 120, 'enemy_2'),
                Bullet((self.rect.centerx, self.rect.top + 10), 2, 150, 'enemy_2'),
            ]
        elif self.type == 3:
            degrees = self.__bullet_direction * 20
            self.__bullet_direction = (self.__bullet_direction + 1) % 10

            bullets = Bullet((self.rect.centerx, self.rect.top), 2, degrees, 'enemy_3')

        return bullets


class SmallFairy(Enemy):
    def __init__(self, enemy_type: int):
        """Inicializa uma nova instância da classe SmallFairy.

        Parameters
        ----------
        enemy_type : int
            O tipo do inimigo.
        """
        super().__init__(4, 800)

        self.type = enemy_type

        self.__sprites = [pygame.image.load(f"assets/images/enemies/fairy{self.type + 3}_{i}.png") for i in range(4)]

        self.image = self.__sprites[0]

        # Configurações de animação
        self.__animation_count = 0
        self.__last_frame_time = 0 
        self.__animation_cooldown = 70
        
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.x = random.randint(20, 780)
        
        # Configurações de velocidade
        self.__x_speed = random.uniform(-0.8, 0.8)
        self.__y_speed = random.uniform(0.8, 0.9)

    def update_animation(self):
        """Atualiza a animação do inimigo.
        """
        current_time = pygame.time.get_ticks()

        if current_time - self.__last_frame_time > self.__animation_cooldown:
            self.__last_frame_time = pygame.time.get_ticks()

            self.__animation_count += 1

            if self.__animation_count >= len(self.__sprites):
                self.__animation_count = 0

            self.image = self.__sprites[self.__animation_count]

    def move(self):
        """Move o inimigo.
        """
        self.rect.x += self.__x_speed
        self.rect.y += self.__y_speed

        if self.rect.left <= 0 or self.rect.right >= 800:
            self.__x_speed *= -1
    
    def update_hitbox(self):
        """Atualiza a hitbox do inimigo.
        """
        self.hitbox = (self.rect.x, self.rect.y, 30, 30)
    
    def recharge(self) -> pygame.sprite.Group:
        """Obtém as balas disparadas pelo inimigo.

        Returns
        -------
        pygame.sprite.Group
            O grupo de sprites com os novos tiros.
        """
        degrees = random.randint(0, 180)

        bullet = Bullet((self.rect.centerx, self.rect.top), 2, degrees, 'enemy_4')

        return bullet