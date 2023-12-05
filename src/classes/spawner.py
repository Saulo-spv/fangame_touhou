import pygame
import random
from classes.enemies import*

class Spawn:
    def __init__ (self, all_enemies):
        self.all_enemies = all_enemies
        self._last_spawn_time = 0
        self.small_type = 1

        # Quantidade máxima de inimigos
        self.max_small_type = 4
        self.max_big_type1 = 1
        self.max_big_type2 = 0
        self.max_big_type3 = 0


    def spawn(self):
        current_time = pygame.time.get_ticks()

        if current_time > 10000 and current_time < 10100:
            self.max_small_type = 5
            self.max_big_type1 = 2
            self.max_big_type2 = 1
        elif current_time > 20000 and current_time < 20100:
            self.max_small_type = 6
            self.max_big_type1 = 2
            self.max_big_type2 = 1
        elif current_time > 30000 and current_time < 30100:
            self.max_small_type = 18
            self.max_big_type1 = 0
            self.max_big_type2 = 2
            self.max_big_type3 = 3
            self.small_type = 2

        self.mob_spawner()

    def mob_spawner(self):
        big_type1_count = sum(isinstance(sprite, BigFairyType1) for sprite in self.all_enemies.sprites())
        big_type2_count = sum(isinstance(sprite, BigFairyType2) for sprite in self.all_enemies.sprites())
        big_type3_count = sum(isinstance(sprite, BigFairyType3) for sprite in self.all_enemies.sprites())
        small_type_count = sum(isinstance(sprite, SmallFairy) for sprite in self.all_enemies.sprites())
        self.mob_spawner_aux(big_type1_count, big_type2_count, big_type3_count, small_type_count)

    def mob_spawner_aux(self, big_type1_count, big_type2_count, big_type3_count, small_type_count):
            if small_type_count < self.max_small_type:
                current_time = pygame.time.get_ticks()
                if current_time - self._last_spawn_time > random.randint(900,1200):
                    self._last_spawn_time = current_time
                    self.all_enemies.add(SmallFairy(self.small_type))

            if big_type1_count < self.max_big_type1:
                current_time = pygame.time.get_ticks()
                if current_time - self._last_spawn_time > random.randint(1300, 1600):
                    self._last_spawn_time = current_time
                    self.all_enemies.add(BigFairyType1())

            if big_type2_count < self.max_big_type2:
                current_time = pygame.time.get_ticks()
                if current_time - self._last_spawn_time > random.randint(1300, 1600):
                    self._last_spawn_time = current_time
                    self.all_enemies.add(BigFairyType2())

            if big_type3_count < self.max_big_type3:
                current_time = pygame.time.get_ticks()
                if current_time - self._last_spawn_time > random.randint(1000, 1200):
                    self._last_spawn_time = current_time
                    self.all_enemies.add(BigFairyType3())