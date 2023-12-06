import pygame
import random
from classes.enemies import*

class Spawn:

    INTERVAL_1 = 15000
    INTERVAL_2 = 30000
    INTERVAL_3 = 45000
    INTERVAL_4 = 80000

    def __init__ (self, all_enemies):
        # pygame.group dos inimigos
        self.all_enemies = all_enemies

        # Variáveis de controle
        self.types = [SmallFairy, BigFairyType1, BigFairyType2, BigFairyType3]
        self.max_quantity = [4,1,0,0]
        self.small_type = 1

        # Tempo do último spwan
        self._last_spawn_time = 0

        # Delay no surgimento
        self.cooldown = 3500

    def spawn(self):
        current_time = pygame.time.get_ticks()

        # Alteração das variáveis de controle conforme o tempo
        if self.INTERVAL_1 < current_time < self.INTERVAL_1 + 100:
            self.max_quantity = [5,2,0,0]
            self.cooldown = 2000

        elif self.INTERVAL_2 < current_time < self.INTERVAL_2 + 100:
            self.max_quantity = [6,2,1,0]
            self.cooldown = 1200

        elif self.INTERVAL_3 < current_time < self.INTERVAL_3 + 100:
            self.max_quantity = [9,0,2,3]
            self.small_type = 2
            self.cooldown = 900

        elif self.INTERVAL_4 < current_time < self.INTERVAL_4 + 100:
            self.max_quantity = [16,5,3,0]
            self.small_type = 1
            self.cooldown = 500

        self.mob_spawner()
        
    def mob_spawner(self):
        quantities = []

        # Registro da quantidade de inimigos vigentes
        for fairy_type in self.types:
            count = sum(isinstance(sprite, fairy_type) for sprite in self.all_enemies.sprites())
            quantities.append(count)

        self.mob_spawner_aux(quantities)

    def mob_spawner_aux(self, quantities):
        current_time = pygame.time.get_ticks()
        
        # Adiciona novos inimigos
        for i in range(4):
            if quantities[i] < self.max_quantity[i]:
                current_time = pygame.time.get_ticks()
                if current_time - self._last_spawn_time > self.cooldown:
                    self._last_spawn_time = current_time
                    if i == 0:
                        self.all_enemies.add(self.types[i](self.small_type))
                    else:
                        self.all_enemies.add(self.types[i]())