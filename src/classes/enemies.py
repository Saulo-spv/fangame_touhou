import pygame
import random
from abc import ABC, abstractmethod

from classes.bullets import *
from classes.entity import Entity


class Enemy(Entity, ABC):
    def __init__(self, life, shoot_cooldown):
        super().__init__(life, shoot_cooldown)

        self._shoot_cooldown = shoot_cooldown

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def update_animation(self):
        pass

    @abstractmethod
    def update_hitbox(self):
        pass

    @abstractmethod
    def recharge(self):
        pass

    def screen_limit(self):
        if self.rect.top >= 600:
            self.kill()


class BigFairy(Enemy):
    def __init__(self, enemy_type):
        self.type = enemy_type

        self._sprites = [pygame.image.load(f"assets/images/enemies/fairy{self.type}_{i}.png") for i in range(4)]
        self._sprites_turn = [pygame.image.load(f"assets/images/enemies/turn{self.type}_{i}.png") for i in range(4)]

        self.image = self._sprites[0]

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

        self._bullet_direction = 0

        if self.type == 3:
            shoot_cooldown = 400
        else:
            shoot_cooldown = 1500

        super().__init__(10, shoot_cooldown)

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
    
    def update_hitbox(self):
        self.hitbox = (self.rect.x, self.rect.y, 50, 50)
    
    def recharge(self):
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
            degrees = self._bullet_direction * 20
            self._bullet_direction = (self._bullet_direction + 1) % 10

            bullets = Bullet((self.rect.centerx, self.rect.top), 2, degrees, 'enemy_3')

        return bullets


class SmallFairy(Enemy):
    def __init__(self, enemy_type):
        super().__init__(4, 800)

        self.type = enemy_type

        self._sprites = [pygame.image.load(f"assets/images/enemies/fairy{self.type + 3}_{i}.png") for i in range(4)]

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
    
    def update_hitbox(self):
        self.hitbox = (self.rect.x, self.rect.y, 30, 30)
    
    def recharge(self):
        degrees = random.randint(0, 180)

        bullet = Bullet((self.rect.centerx, self.rect.top), 2, degrees, 'enemy_4')

        return bullet