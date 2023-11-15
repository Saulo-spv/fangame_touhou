import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, x, y, width, height, sprite_width, sprite_height, screen_height, screen_width):
        super().__init__()

        # Configurações iniciais do jogador
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.current_line = 0
        self.current_frame = 0
        self.sprite_sheet = sprite_sheet

        # Configura a imagem inicial do jogador
        self.image = self.sprite_sheet.subsurface(pygame.Rect(self.x, self.y, self.sprite_width, self.sprite_height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, self.screen_height - 50)

        self.speed = 5

    def update(self, keys):
        # Configura a movimentação
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            self.current_line = 1
            self.rect.y -= self.speed / 3**0.5
            self.rect.x -= self.speed / 3**0.5
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            self.current_line = 2
            self.rect.y -= self.speed / 3**0.5
            self.rect.x += self.speed / 3**0.5
        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            self.current_line = 2
            self.rect.y += self.speed / 3**0.5
            self.rect.x += self.speed / 3**0.5
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self.current_line = 1
            self.rect.y += self.speed / 3**0.5
            self.rect.x -= self.speed / 3**0.5
        elif keys[pygame.K_LEFT]:
            self.current_line = 1
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.current_line = 2
            self.rect.x += self.speed
        elif keys[pygame.K_DOWN]:
            self.current_line = 0
            self.rect.y += self.speed
        elif keys[pygame.K_UP]:
            self.current_line = 0
            self.rect.y -= self.speed
        else:
            self.current_line = 0

        self.screen_limit()

        self.update_animation()

    def screen_limit(self):
        # Garante que o jogador não ultrapasse as bordas da tela
        self.rect.x = max(-10, min(self.rect.x, self.screen_width - self.sprite_width * 1.5))
        self.rect.y = max(-5, min(self.rect.y, self.screen_height - self.sprite_height * 1.2))

    def update_animation(self):
        # Velocidade da animação
        animation_speed = 5
        self.current_frame = (self.current_frame + 1) % (8 * animation_speed)

        # Ajuste a velocidade da animação
        self.y = self.current_line * self.sprite_height
        self.x = (self.current_frame // animation_speed) * self.sprite_width

        # Atualiza a imagem do jogador com a parte correta do sprite sheet
        self.image = self.sprite_sheet.subsurface(pygame.Rect(self.x, self.y, self.sprite_width, self.sprite_height)).convert_alpha()

        self.image = pygame.transform.scale(self.image, (60,60))
