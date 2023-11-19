import pygame
from abc import ABC, abstractmethod


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

    def spawn_bullets(self):
        bullets = self.recharge()
            
        self._last_shoot_time = pygame.time.get_ticks()

        return bullets
    
    def can_shoot(self):
        # Verifica se o tempo desde o último tiro é maior que o cooldown
        now = pygame.time.get_ticks()
        return now - self._last_shoot_time > self._shoot_cooldown
    
    def update(self):
        self.move()
        self.screen_limit()
        self.update_animation()