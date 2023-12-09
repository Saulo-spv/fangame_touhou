"""Classe PowerUp

Módulo responsável por implementar a classe PowerUp, que representa um power-up do jogo.

"""
import pygame

from classes.player import Player


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], type: str, player: Player, enemy_bullets: pygame.sprite.Group):
        """Inicializa uma nova instância da classe PowerUp.

        Parameters
        ----------
        pos : tuple[int, int]
            A posição inicial do power-up.
        type : str
            O tipo do power-up.
        player : _type_
            O jogador.
        """
        super().__init__()

        self.type = type

        # Configura a imagem do power-up
        if self.type == 'life':
            self.image = pygame.image.load('assets/images/power_ups/life_potion.png').convert_alpha()
        elif self.type == 'shield':
            self.image = pygame.image.load('assets/images/power_ups/shield.png').convert_alpha()
        elif self.type == 'clear_bullets':
            self.image = pygame.image.load('assets/images/power_ups/clear_bullets.png').convert_alpha()
        
        self.image = pygame.transform.scale(self.image, (30, 30))
        
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.hitbox = self.rect

        self.__player = player
        self.__enemy_bullets = enemy_bullets
    
    @property
    def hitbox(self) -> pygame.Rect:
        """Obtém a hitbox do power-up.

        Returns
        -------
        pygame.Rect
            A hitbox do power-up.
        """
        return self.__hitbox

    @hitbox.setter
    def hitbox(self, values: tuple[int, int, int, int]):
        """Define a hitbox do power-up.

        Parameters
        ----------
        values : tuple[int, int, int, int]
            Os valores da hitbox do power-up.
        """
        x, y, width, height = values
        self.__hitbox = pygame.Rect(x, y, width, height)
    
    def collect(self):
        """Coleta o power-up.
        """
        if self.type == 'life':
            if self.__player.life < 5:
                self.__player.life += 1
        elif self.type == 'shield':
            self.__player.shield = True
        elif self.type == 'clear_bullets':
            for bullet in self.__enemy_bullets:
                bullet.kill()

        self.kill()
    
    def update(self):
        """Atualiza o power-up.
        """
        self.rect.y += 1

        self.hitbox = self.rect

        if self.rect.top >= 600:
            self.kill()