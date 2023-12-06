import pygame
from abc import ABC, abstractmethod


class Entity(ABC, pygame.sprite.Sprite):
    def __init__(self, life, shoot_cooldown):
        super().__init__()

        self.__life = life
        self.__last_shoot_time = 0
        self.__shoot_cooldown = shoot_cooldown

    @property
    def life(self):
        return self.__life
    
    @life.setter
    def life(self, value):
        self.__life = value
    
    @property
    def last_shoot_time(self):
        return self.__last_shoot_time
    
    @last_shoot_time.setter
    def last_shoot_time(self, time):
        self.__last_shoot_time = time

    @property
    def shoot_cooldown(self):
        return self.__shoot_cooldown
    
    @shoot_cooldown.setter
    def shoot_cooldown(self, value):
        self.__shoot_cooldown = value

    @property
    def hitbox(self):
        return self.__hitbox
    
    @hitbox.setter
    def hitbox(self, values):
        x, y, width, height = values
        self.__hitbox = pygame.Rect(x, y, width, height)

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
    def update_hitbox(self):
        pass

    @abstractmethod
    def recharge(self):
        pass

    def spawn_bullets(self):
        bullets = self.recharge()
            
        self.last_shoot_time = pygame.time.get_ticks()

        return bullets
    
    def can_shoot(self):
        # Verifica se o tempo desde o último tiro é maior que o cooldown
        now = pygame.time.get_ticks()
        return now - self.last_shoot_time > self.shoot_cooldown
    
    def get_hit(self):
        self.life -= 1

        if self.life == 0:
            self.kill()
    
    def update(self):
        self.move()
        self.screen_limit()
        self.update_animation()
        self.update_hitbox()