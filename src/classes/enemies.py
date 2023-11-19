import pygame
import random
from abc import ABC, abstractmethod

from classes.bullets import *
from classes.entity import Entity


class Enemy(Entity, ABC):
    def __init__(self, shoot_cooldown):
        super().__init__(shoot_cooldown)

        self._shoot_cooldown = shoot_cooldown

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def update_animation(self):
        pass

    @abstractmethod
    def recharge(self):
        pass

    def screen_limit(self):
        if self.rect.top >= 600:
            self.kill()


class BigFairy(Enemy, ABC):
    def __init__(self, default_image, shoot_cooldown):
        super().__init__(shoot_cooldown)

        self.image = default_image

        # Configurações de animação
        self._animation_count = 0
        self._last_frame_time = 0
        self._animation_cooldown = 70

        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.x = random.randint(20, 780)

        # Configurações de velocidade
        self._x_speed = random.uniform(-2, 2)
        self._y_speed = random.uniform(1.7, 1.8)
        self._stay_y = random.randint(100, 300)

    def update_animation(self):
        current_time = pygame.time.get_ticks()

        if self._x_speed == 0:
            if current_time - self._last_frame_time > self._animation_cooldown:
                self._last_frame_time = pygame.time.get_ticks()
                self._animation_count += 1

                if self._animation_count >= len(self._sprites):
                    self._animation_count = 0

                self.image = self._sprites[self._animation_count]
        elif self._x_speed < 0:
            if current_time - self._last_frame_time > self._animation_cooldown:
                self._last_frame_time = pygame.time.get_ticks()
                self._animation_count += 1

                if self._animation_count >= len(self._sprites_turn):
                    self._animation_count = 0

                flipped_turn = pygame.transform.flip(self._sprites_turn[self._animation_count], True, False)

                self.image = flipped_turn
        elif self._x_speed > 0:
            if current_time - self._last_frame_time > self._animation_cooldown:
                self._last_frame_time = pygame.time.get_ticks()
                self._animation_count += 1

                if self._animation_count >= len(self._sprites_turn):
                    self._animation_count = 0

                self.image = self._sprites_turn[self._animation_count]

    def move(self):
        if self.rect.y >= self._stay_y:
            self._x_speed = 0
            self._y_speed = 0
        else:
            self.rect.x += self._x_speed
            self.rect.y += self._y_speed

            if self.rect.left <= 0 or self.rect.right >= 800:
                self._x_speed *= -1
    
    @abstractmethod
    def recharge(self):
        pass


class SmallFairy(Enemy):
    def __init__(self, enemy_type):
        super().__init__(800)

        if enemy_type == 1:
            self._sprites = [
                pygame.image.load("assets/images/enemies/fairy4_0.png"), 
                pygame.image.load("assets/images/enemies/fairy4_1.png"), 
                pygame.image.load("assets/images/enemies/fairy4_2.png"), 
                pygame.image.load("assets/images/enemies/fairy4_3.png")
            ]
        elif enemy_type == 2:
            self._sprites = [
                pygame.image.load("assets/images/enemies/fairy5_0.png"), 
                pygame.image.load("assets/images/enemies/fairy5_1.png"), 
                pygame.image.load("assets/images/enemies/fairy5_2.png"), 
                pygame.image.load("assets/images/enemies/fairy5_3.png")
            ]

        self.image = self._sprites[0]

        # Configurações de animação
        self._animation_count = 0
        self._last_frame_time = 0 
        self._animation_cooldown = 70
        
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.x = random.randint(20, 780)
        
        # Configurações de velocidade
        self._x_speed = random.uniform(-0.8, 0.8)
        self._y_speed = random.uniform(0.8, 0.9)

    def update_animation(self):
        current_time = pygame.time.get_ticks()

        if current_time - self._last_frame_time > self._animation_cooldown:
            self._last_frame_time = pygame.time.get_ticks()

            self._animation_count += 1

            if self._animation_count >= len(self._sprites):
                self._animation_count = 0

            self.image = self._sprites[self._animation_count]

    def move(self):
        self.rect.x += self._x_speed
        self.rect.y += self._y_speed

        if self.rect.left <= 0 or self.rect.right >= 800:
            self._x_speed *= -1
    
    def recharge(self):
        degrees = random.randint(0, 180)

        # Cria um novo tiro e o adiciona ao grupo de sprites
        bullet = EnemyBullet((self.rect.centerx, self.rect.top), degrees, type=4)

        return bullet


class BigFairyType1(BigFairy):    
    def __init__(self):
        self._sprites = [
            pygame.image.load("assets/images/enemies/fairy1_0.png"), 
            pygame.image.load("assets/images/enemies/fairy1_1.png"), 
            pygame.image.load("assets/images/enemies/fairy1_2.png"), 
            pygame.image.load("assets/images/enemies/fairy1_3.png")
        ]

        self._sprites_turn =  [
            pygame.image.load("assets/images/enemies/turn1_0.png"), 
            pygame.image.load("assets/images/enemies/turn1_1.png"), 
            pygame.image.load("assets/images/enemies/turn1_2.png"), 
            pygame.image.load("assets/images/enemies/turn1_3.png")
        ]

        super().__init__(self._sprites[0], 1500)
    
    def recharge(self):
        # Cria os novos tiros e os adicionam ao grupo de sprites
        bullets = [
            EnemyBullet((self.rect.centerx, self.rect.centery), 0, type=1),
            EnemyBullet((self.rect.centerx, self.rect.centery), 90, type=1),
            EnemyBullet((self.rect.centerx, self.rect.centery), 180, type=1),
            EnemyBullet((self.rect.centerx, self.rect.centery), 270, type=1),
        ]

        return bullets


class BigFairyType2(BigFairy):
    def __init__(self):
        self._sprites = [
            pygame.image.load("assets/images/enemies/fairy2_0.png"), 
            pygame.image.load("assets/images/enemies/fairy2_1.png"), 
            pygame.image.load("assets/images/enemies/fairy2_2.png"), 
            pygame.image.load("assets/images/enemies/fairy2_3.png")
        ]

        self._sprites_turn =  [
            pygame.image.load("assets/images/enemies/turn2_0.png"), 
            pygame.image.load("assets/images/enemies/turn2_1.png"), 
            pygame.image.load("assets/images/enemies/turn2_2.png"), 
            pygame.image.load("assets/images/enemies/turn2_3.png")
        ]

        super().__init__(self._sprites[0], 1500)
    
    def recharge(self):
        # Cria os novos tiros e os adicionam ao grupo de sprites
        bullets = [
            EnemyBullet((self.rect.centerx, self.rect.top + 10), 30, type=2),
            EnemyBullet((self.rect.centerx, self.rect.top + 10), 60, type=2),
            EnemyBullet((self.rect.centerx, self.rect.top + 10), 90, type=2),
            EnemyBullet((self.rect.centerx, self.rect.top + 10), 120, type=2),
            EnemyBullet((self.rect.centerx, self.rect.top + 10), 150, type=2),
        ]

        return bullets
    

class BigFairyType3(BigFairy):
    def __init__(self):
        self._sprites = [
            pygame.image.load("assets/images/enemies/fairy3_0.png"), 
            pygame.image.load("assets/images/enemies/fairy3_1.png"), 
            pygame.image.load("assets/images/enemies/fairy3_2.png"), 
            pygame.image.load("assets/images/enemies/fairy3_3.png")
        ]

        self._sprites_turn =  [
            pygame.image.load("assets/images/enemies/turn3_0.png"), 
            pygame.image.load("assets/images/enemies/turn3_1.png"), 
            pygame.image.load("assets/images/enemies/turn3_2.png"), 
            pygame.image.load("assets/images/enemies/turn3_3.png")
        ]

        super().__init__(self._sprites[0], 400)

        self._bullet_direction = 0
    
    def recharge(self):
        degrees = self._bullet_direction * 20
        self._bullet_direction = (self._bullet_direction + 1) % 10

        # Cria um novo tiro e o adiciona ao grupo de sprites
        bullet = EnemyBullet((self.rect.centerx, self.rect.top), degrees, type=3)

        return bullet