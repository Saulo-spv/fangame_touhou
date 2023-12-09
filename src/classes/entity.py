"""Classe Entity.

Módulo responsável por implementar a classe Entity, que representa uma entidade do jogo.

"""
import pygame
from abc import ABC, abstractmethod


class Entity(ABC, pygame.sprite.Sprite):
    def __init__(self, life: int, shoot_cooldown: int):
        """Inicializa uma nova instância da classe Entity.

        Parameters
        ----------
        life : int
            A quantidade inicial de vida da entidade.
        shoot_cooldown : int
            O tempo de espera entre disparos.
        """
        super().__init__()

        self.life = life
        self.last_shoot_time = 0
        self.shoot_cooldown = shoot_cooldown

    @property
    def life(self) -> int:
        """Obtém a quantidade de vida da entidade.

        Returns
        -------
        int
            A quantidade de vida da entidade.
        """
        return self.__life
    
    @life.setter
    def life(self, value: int):
        """Define a quantidade de vida da entidade.

        Parameters
        ----------
        value : int
            A nova quantidade de vida da entidade.
        """
        self.__life = value
    
    @property
    def last_shoot_time(self):
        """Obtém o tempo do último disparo.

        Returns
        -------
        int
            O tempo do último disparo.
        """
        return self.__last_shoot_time
    
    @last_shoot_time.setter
    def last_shoot_time(self, time):
        """Define o tempo do último disparo.

        Parameters
        ----------
        time : int
            O novo tempo do último disparo.
        """
        self.__last_shoot_time = time

    @property
    def shoot_cooldown(self) -> int:
        """Obtém o tempo de espera entre disparos.

        Returns
        -------
        int
            O tempo de espera entre disparos.
        """
        return self.__shoot_cooldown
    
    @shoot_cooldown.setter
    def shoot_cooldown(self, value):
        """Define o tempo de espera entre disparos.

        Parameters
        ----------
        value : int
            O novo tempo de espera entre disparos.
        """
        self.__shoot_cooldown = value

    @property
    def hitbox(self) -> pygame.Rect:
        """Obtém a hitbox da entidade.

        Returns
        -------
        pygame.Rect
            A hitbox da entidade.
        """
        return self.__hitbox
    
    @hitbox.setter
    def hitbox(self, values):
        """Define a hitbox da entidade.

        Parameters
        ----------
        values : tuple[int, int, int, int]
            Os valores da hitbox da entidade.
        """
        x, y, width, height = values
        self.__hitbox = pygame.Rect(x, y, width, height)

    @abstractmethod
    def move(self):
        """Move a entidade.
        """
        pass

    @abstractmethod
    def screen_limit(self):
        """Garante que a entidade ultrapasse os limites da tela.
        """
        pass

    @abstractmethod
    def update_animation(self):
        """Atualiza a animação da entidade.
        """
        pass

    @abstractmethod
    def update_hitbox(self):
        """Atualiza a hitbox da entidade.
        """
        pass

    @abstractmethod
    def recharge(self):
        """Obtém o tiro gerado pela entidade.
        """
        pass

    def spawn_bullets(self) -> pygame.sprite.Group:
        """Cria os novos tiros da entidade.

        Returns
        -------
        pygame.sprite.Group
            O grupo de sprites com o novo tiro.
        """
        bullets = self.recharge()
            
        self.last_shoot_time = pygame.time.get_ticks()

        return bullets
    
    def can_shoot(self) -> bool:
        """Verifica se a entidade pode atirar.

        Returns
        -------
        bool
            True se a entidade pode atirar, False caso contrário.
        """
        now = pygame.time.get_ticks()

        # Verifica se o tempo desde o último tiro é maior que o cooldown
        return now - self.last_shoot_time > self.shoot_cooldown
    
    def get_hit(self):
        """Diminui a vida da entidade em 1.
        """
        self.life -= 1

        if self.life == 0:

            self.kill()
    
    def update(self):
        """Atualiza a entidade.
        """
        self.move()
        self.screen_limit()
        self.update_animation()
        self.update_hitbox()