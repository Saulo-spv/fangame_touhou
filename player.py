import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, x, y, width, height, sprite_width, sprite_height, screen_height, screen_width):
        super().__init__()

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

        self.image = self.sprite_sheet.subsurface(pygame.Rect(self.x, self.y, self.sprite_width, self.sprite_height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, self.screen_height - 50)

        self.speed = 5

    def update(self, keys):
        # Movimentação
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
        elif keys[pygame.K_UP] and self.rect.top > 0:
            self.current_line = 0
            self.rect.y -= self.speed
        else:
            self.current_line = 0

        self.update_animation()

    def update_animation(self):
        animation_speed = 5
        self.current_frame = (self.current_frame + 1) % (8 * animation_speed)
        self.y = self.current_line * self.sprite_height
        self.x = (self.current_frame // animation_speed) * self.sprite_width

        self.image = self.sprite_sheet.subsurface(pygame.Rect(self.x, self.y, self.sprite_width, self.sprite_height)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,60))
