import pygame
import random
from classes.enemies import*

class Spawn:
    def __init__ (self, all_enemies):
        self.all_enemies = all_enemies
        self._last_spawn_time = 0

    def spawn(self):
        big_type1_number = sum(isinstance(sprite, BigFairyType1) for sprite in self.all_enemies.sprites())
        small_type1_number = sum(isinstance(sprite, SmallFairy) for sprite in self.all_enemies.sprites())

        current_time = pygame.time.get_ticks()
        if current_time < 10000:

            if small_type1_number < 6:
                current_time = pygame.time.get_ticks()
                if current_time - self._last_spawn_time > random.randint(600,1200):
                    self._last_spawn_time = current_time
                    self.all_enemies.add(SmallFairy(1))

            if big_type1_number < 5:
                current_time = pygame.time.get_ticks()
                if current_time - self._last_spawn_time > random.randint(900, 1500):
                    self._last_spawn_time = current_time
                    prob = random.randint(1,100)
                    if prob < 95:
                        self.all_enemies.add(BigFairyType1())
                    else:
                        self.all_enemies.add(BigFairyType2())

        else:

            if small_type1_number < 10:
                if current_time - self._last_spawn_time > random.randint(500,1100):
                    self._last_spawn_time = current_time
                    self.all_enemies.add(SmallFairy(random.randint(1,2)))

            if big_type1_number < 6:
                current_time = pygame.time.get_ticks()
                if current_time - self._last_spawn_time > random.randint(800, 1400):
                    self._last_spawn_time = current_time
                    prob = random.randint(1,100)
                    if prob < 90:
                        self.all_enemies.add(BigFairyType1())



    