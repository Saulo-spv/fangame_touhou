"""Classe Player

Módulo responsável por implementar a classe Player, que representa o jogador do jogo.
    
"""
import pygame

from classes.entity import Entity
from classes.bullets import Bullet


class Player(Entity):
    def __init__(self):
        """Inicializa uma nova instância da classe Player.
        """
        super().__init__(3, 150)

        # Configurações dos sprites
        self.__sprite_sheet_x = 0
        self.__sprite_sheet_y = 0
        self.__current_line = 0
        self.__current_frame = 0
        self.__animation_speed = 7
        self.__sprite_sheet = pygame.image.load("assets/images/player/sprite_sheet.png")

        # Configura a imagem inicial do jogador
        self.image = self.__sprite_sheet.subsurface(pygame.Rect(self.__sprite_sheet_x, self.__sprite_sheet_y, 32, 46)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)

        # Velocidade do jogador
        self.__speed = 5

        self.shield = False
    
    @property
    def shield(self) -> bool:
        """Obtém o valor de shield.

        Returns
        -------
        bool
            O valor de shield.
        """
        return self.__shield

    @shield.setter
    def shield(self, value: bool):
        """Define o valor de shield.

        Parameters
        ----------
        value : bool
            O novo valor de shield.
        """
        self.__shield = value

    def move(self):
        """Move o jogador de acordo com as teclas pressionadas.
        """
        # Configura a movimentação
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and keys[pygame.K_a]:
            self.__current_line = 1
            self.rect.y -= self.__speed / 3**0.5
            self.rect.x -= self.__speed / 3**0.5
        elif keys[pygame.K_w] and keys[pygame.K_d]:
            self.__current_line = 2
            self.rect.y -= self.__speed / 3**0.5
            self.rect.x += self.__speed / 3**0.5
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            self.__current_line = 2
            self.rect.y += self.__speed / 3**0.5
            self.rect.x += self.__speed / 3**0.5
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            self.__current_line = 1
            self.rect.y += self.__speed / 3**0.5
            self.rect.x -= self.__speed / 3**0.5
        elif keys[pygame.K_a]:
            self.__current_line = 1
            self.rect.x -= self.__speed
        elif keys[pygame.K_d]:
            self.__current_line = 2
            self.rect.x += self.__speed
        elif keys[pygame.K_s]:
            self.__current_line = 0
            self.rect.y += self.__speed
        elif keys[pygame.K_w]:
            self.__current_line = 0
            self.rect.y -= self.__speed
        else:
            self.__current_line = 0

    def screen_limit(self):
        """Garante que o jogador não ultrapasse as bordas da tela.
        """
        # Garante que o jogador não ultrapasse as bordas da tela
        self.rect.x = max(-10, min(self.rect.x, 740))
        self.rect.y = max(-5, min(self.rect.y, 540))

    def recharge(self) -> Bullet:
        """Cria um novo tiro para o Player.

        Returns
        -------
        Bullet
            O tiro criado.
        """
        # Cria um novo tiro e o adiciona ao grupo de sprites
        bullet = Bullet((self.rect.centerx, self.rect.top), 10, -90, 'player')
        
        return bullet

    def update_animation(self):
        """Atualiza a animação do jogador.
        """
        # Encontra o sprite para o frame atual
        self.__current_frame = (self.__current_frame + 1) % (8 * self.__animation_speed)
        self.__sprite_sheet_x = (self.__current_frame // self.__animation_speed) * 32
        self.__sprite_sheet_y = self.__current_line * 46

        # Atualiza a imagem do jogador com a parte correta do sprite sheet
        self.image = self.__sprite_sheet.subsurface(pygame.Rect(self.__sprite_sheet_x, self.__sprite_sheet_y, 32, 46)).convert_alpha()

        self.image = pygame.transform.scale(self.image, (60, 60))
    
    def update_hitbox(self):
        """Atualiza a hitbox do jogador.
        """
        self.hitbox = (self.rect.centerx + 8, self.rect.centery + 5, 10, 10)