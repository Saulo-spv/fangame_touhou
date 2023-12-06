import pygame
import random
from classes.enemies import*

class Spawn:

    INTERVAL_1 = 20000
    INTERVAL_2 = 40000
    INTERVAL_3 = 60000
    INTERVAL_4 = 90000

    def __init__ (self, all_enemies):
        # pygame.group dos inimigos
        self.all_enemies = all_enemies

        # Variáveis de controle
        self.types = {SmallFairy:2, BigFairy:3}
        self.max_quantity = {SmallFairy:[2,0], BigFairy:[0,0,0]}

        # Tempo do último spwan
        self._last_spawn_time = {SmallFairy:[0,0], BigFairy:[0,0,0]}

        # Delay no surgimento
        self.cooldown = 2500

    def spawn(self):
        current_time = pygame.time.get_ticks()

        # Alteração das variáveis de controle conforme o tempo
        if self.INTERVAL_1 < current_time < self.INTERVAL_1 + 100:
            self.max_quantity = {SmallFairy:[3,0], BigFairy:[1,0,0]}
            self.cooldown = 2000

        elif self.INTERVAL_2 < current_time < self.INTERVAL_2 + 100:
            self.max_quantity = {SmallFairy:[3,0], BigFairy:[1,1,0]}
            self.cooldown = 1200

        elif self.INTERVAL_3 < current_time < self.INTERVAL_3 + 100:
            self.max_quantity = {SmallFairy:[5,1], BigFairy:[2,1,0]}
            self.cooldown = 900

        elif self.INTERVAL_4 < current_time < self.INTERVAL_4 + 100:
            self.max_quantity = {SmallFairy:[2,6], BigFairy:[0,2,3]}
            self.cooldown = 500

        self.mob_spawner()
        
    def mob_spawner(self):
        quantities = {SmallFairy:[], BigFairy:[]}
        # Registro da quantidade de inimigos vigentes
        for fairy_type in self.types:
            for i in range(self.types[fairy_type]):
                count = sum(isinstance(sprite, fairy_type) and sprite.type == i+1 for sprite in self.all_enemies.sprites())
                quantities[fairy_type].append(count)

        self.mob_spawner_aux(quantities)

    def mob_spawner_aux(self, quantities):
        current_time = pygame.time.get_ticks()
        # Adiciona novos inimigos
        for fairy_type in self.types:
            for i in range(self.types[fairy_type]):
                if quantities[fairy_type][i] < self.max_quantity[fairy_type][i]:
                    current_time = pygame.time.get_ticks()
                    if current_time - self._last_spawn_time[fairy_type][i] > self.cooldown:
                        self._last_spawn_time[fairy_type][i] = current_time
                        self.all_enemies.add(fairy_type(i+1))