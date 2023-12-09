"""Classe Spawn

Módulo responsável por implementar a classe Spawn, que representa o spawner de inimigos do jogo.

"""
import pygame

from classes.enemies import*


class Spawn:
    # Intervalos de tempo
    INTERVAL_1 = 20000
    INTERVAL_2 = 40000
    INTERVAL_3 = 60000
    INTERVAL_4 = 90000

    def __init__ (self, all_enemies: pygame.sprite.Group):
        """Inicializa uma nova instância da classe Spawn.

        Parameters
        ----------
        all_enemies : pygame.sprite.Group
            O grupo de sprites com todos os inimigos.
        """
        # pygame.group dos inimigos
        self.all_enemies = all_enemies

        # Variáveis de controle
        self.types = {SmallFairy:2, BigFairy:3}
        self.max_quantity = {SmallFairy:[2,0], BigFairy:[0,0,0]}
        self.current_time = 0

        # Tempo do último spwan
        self.__last_spawn_time = {SmallFairy:[0,0], BigFairy:[0,0,0]}

        # Delay no surgimento
        self.cooldown = 2500

    def spawn(self):
        """Spawna os inimigos de acordo com o tempo.
        """
        # Alteração das variáveis de controle conforme o tempo
        if self.INTERVAL_1 < self.current_time < self.INTERVAL_1 + 100:
            self.max_quantity = {SmallFairy:[3,0], BigFairy:[1,0,0]}
            self.cooldown = 2000

        elif self.INTERVAL_2 < self.current_time < self.INTERVAL_2 + 100:
            self.max_quantity = {SmallFairy:[3,0], BigFairy:[1,1,0]}
            self.cooldown = 1200

        elif self.INTERVAL_3 < self.current_time < self.INTERVAL_3 + 100:
            self.max_quantity = {SmallFairy:[5,1], BigFairy:[2,1,0]}
            self.cooldown = 900

        elif self.INTERVAL_4 < self.current_time < self.INTERVAL_4 + 100:
            self.max_quantity = {SmallFairy:[2,6], BigFairy:[0,2,3]}
            self.cooldown = 500

        self.mob_spawner()
        
    def mob_spawner(self):
        """Spawna os inimigos de acordo com as quantidades máximas.
        """
        quantities = {SmallFairy:[], BigFairy:[]}
        # Registro da quantidade de inimigos vigentes
        for fairy_type in self.types:
            for i in range(self.types[fairy_type]):
                count = sum(isinstance(sprite, fairy_type) and sprite.type == i+1 for sprite in self.all_enemies.sprites())
                quantities[fairy_type].append(count)

        self.mob_spawner_aux(quantities)

    def mob_spawner_aux(self, quantities: dict[pygame.sprite.Sprite, list[int]]):
        """Spawna os inimigos de acordo com as quantidades máximas.

        Parameters
        ----------
        quantities : dict[pygame.sprite.Sprite, list[int]]
            Dicionário com as quantidades de cada inimigo.
        """
        current_time = pygame.time.get_ticks()
        # Adiciona novos inimigos
        for fairy_type in self.types:
            for i in range(self.types[fairy_type]):
                # Verifica se a quantidade atual é menor que a máxima
                if quantities[fairy_type][i] < self.max_quantity[fairy_type][i]:
                    current_time = pygame.time.get_ticks()
                    # Verifica se o tempo desde o último spawn é maior que o cooldown
                    if current_time - self.__last_spawn_time[fairy_type][i] > self.cooldown:
                        self.__last_spawn_time[fairy_type][i] = current_time
                        self.all_enemies.add(fairy_type(i+1))

    def reset(self):
        """Reseta as variáveis modificadas em game
        """
        # Reseta as variváveis modificadas em game.py
        self.current_time = 0
        self.max_quantity = {SmallFairy:[2,0], BigFairy:[0,0,0]}
        self.__last_spawn_time = {SmallFairy:[0,0], BigFairy:[0,0,0]}
        self.cooldown = 2500
        self.all_enemies.empty()