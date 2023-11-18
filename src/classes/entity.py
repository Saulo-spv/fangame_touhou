import pygame
from abc import ABC, abstractmethod

from classes.game import Game

class Entity(ABC, pygame.sprite.Sprite):
    def __init__(self, shoot_cooldown):
        super().__init__()

        self._last_shoot_time = 0
        self._shoot_cooldown = shoot_cooldown

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def screen_limit(self):
        pass

    @abstractmethod
    def update_animation(self):
        pass

    @abstractmethod
    def recharge(self):
        pass

    @abstractmethod
    def shoot(self):
        pass

    def fire_bullet(self):
        bullets = self.recharge()

        Game.all_sprites.add(bullets)
        Game.bullets.add(bullets)

        self._last_shoot_time = pygame.time.get_ticks()
    
    def can_shoot(self):
        # Verifica se o tempo desde o último tiro é maior que o cooldown
        now = pygame.time.get_ticks()
        
        return now - self._last_shoot_time > self._shoot_cooldown
    
    def update(self):
        self.move()
        self.screen_limit()
        self.update_animation()
        self.shoot()