import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, all_sprites, bullets):
        super().__init__()

        # Configurações iniciais do jogador
        self.x = 0
        self.y = 0
        self.width = 32
        self.height = 50
        self.sprite_width = 32
        self.sprite_height = 46
        self.screen_height = pygame.display.get_surface().get_height()
        self.screen_width = pygame.display.get_surface().get_width()
        self.current_line = 0
        self.current_frame = 0
        self.sprite_sheet = sprite_sheet

        # Configura a imagem inicial do jogador
        self.image = self.sprite_sheet.subsurface(pygame.Rect(self.x, self.y, self.sprite_width, self.sprite_height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.screen_width // 2, self.screen_height - 50)

        self.speed = 5
        self.all_sprites = all_sprites
        self.bullets = bullets

    def update(self):
        # Configura a movimentação
        keys = pygame.key.get_pressed()
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

        # Dispara o tiro
        if keys[pygame.K_SPACE]:
            self.fire_bullet()

        self.screen_limit()

        self.update_animation()

    def screen_limit(self):
        # Garante que o jogador não ultrapasse as bordas da tela
        self.rect.x = max(-10, min(self.rect.x, self.screen_width - self.sprite_width * 1.5))
        self.rect.y = max(-5, min(self.rect.y, self.screen_height - self.sprite_height * 1.2))

    def fire_bullet(self):
        # Cria um novo tiro e o adiciona ao grupo de sprites
        bullet = Bullet(self.rect.centerx, self.rect.top, self.sprite_sheet)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

    def update_animation(self):
        # Ajusta a velocidade da animação
        animation_speed = 7
        self.current_frame = (self.current_frame + 1) % (8 * animation_speed)
        self.y = self.current_line * self.sprite_height
        self.x = (self.current_frame // animation_speed) * self.sprite_width

        # Atualiza a imagem do jogador com a parte correta do sprite sheet
        self.image = self.sprite_sheet.subsurface(pygame.Rect(self.x, self.y, self.sprite_width, self.sprite_height)).convert_alpha()

        self.image = pygame.transform.scale(self.image, (60, 60))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_sheet):
        super().__init__()

        # Posição do tiro no sprite sheet
        bullet_x = 0
        bullet_y = 150
        bullet_width = 16
        bullet_height = 16 

        # Inicializa e posiciona o tiro
        self.image = sprite_sheet.subsurface(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed

        # Remove o tiro quando atinge o topo da tela
        if self.rect.bottom < 0:
            self.kill()
