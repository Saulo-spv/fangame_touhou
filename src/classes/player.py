import pygame

from classes.entity import Entity
from classes.bullets import PlayerBullet


class Player(Entity):
    def __init__(self):
        super().__init__(200)

        # Configurações dos sprites
        self._sprite_sheet_x = 0
        self._sprite_sheet_y = 0
        self._current_line = 0
        self._current_frame = 0
        self._animation_speed = 7
        self._sprite_sheet = pygame.image.load("assets/images/player/sprite_sheet.png")

        # Configura a imagem inicial do jogador
        self.image = self._sprite_sheet.subsurface(pygame.Rect(self._sprite_sheet_x, self._sprite_sheet_y, 32, 46)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)

        # Velocidade do jogador
        self._speed = 5

    def move(self):
        # Configura a movimentação
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            self._current_line = 1
            self.rect.y -= self._speed / 3**0.5
            self.rect.x -= self._speed / 3**0.5
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            self._current_line = 2
            self.rect.y -= self._speed / 3**0.5
            self.rect.x += self._speed / 3**0.5
        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            self._current_line = 2
            self.rect.y += self._speed / 3**0.5
            self.rect.x += self._speed / 3**0.5
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self._current_line = 1
            self.rect.y += self._speed / 3**0.5
            self.rect.x -= self._speed / 3**0.5
        elif keys[pygame.K_LEFT]:
            self._current_line = 1
            self.rect.x -= self._speed
        elif keys[pygame.K_RIGHT]:
            self._current_line = 2
            self.rect.x += self._speed
        elif keys[pygame.K_DOWN]:
            self._current_line = 0
            self.rect.y += self._speed
        elif keys[pygame.K_UP]:
            self._current_line = 0
            self.rect.y -= self._speed
        else:
            self._current_line = 0

    def screen_limit(self):
        # Garante que o jogador não ultrapasse as bordas da tela
        self.rect.x = max(-10, min(self.rect.x, 740))
        self.rect.y = max(-5, min(self.rect.y, 540))

    def recharge(self):
        # Cria um novo tiro e o adiciona ao grupo de sprites
        bullet = PlayerBullet((self.rect.centerx, self.rect.top))
        
        return bullet

    def update_animation(self):
        # Encontra o sprite para o frame atual
        self._current_frame = (self._current_frame + 1) % (8 * self._animation_speed)
        self._sprite_sheet_x = (self._current_frame // self._animation_speed) * 32
        self._sprite_sheet_y = self._current_line * 46

        # Atualiza a imagem do jogador com a parte correta do sprite sheet
        self.image = self._sprite_sheet.subsurface(pygame.Rect(self._sprite_sheet_x, self._sprite_sheet_y, 32, 46)).convert_alpha()

        self.image = pygame.transform.scale(self.image, (60, 60))