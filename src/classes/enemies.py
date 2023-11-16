import pygame
import random

class Enemy(pygame.sprite.Sprite):
    '''Classe abstrata base dos inimigos'''

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self._speed = random.uniform(0.8, 0.9)

    def update(self):
        self.rect.y += self._speed

        if self.rect.top >= 600:
            self.kill()

class EnemyType1(Enemy):

    ANIMATION_COOLDOWN = 70

    def __init__(self, screen_width, screen_height, default_image):
        super().__init__(screen_width, screen_height)
        self.image = default_image
        self._animation_count = 0
        self._last_frame_time = 0 
        self._animation_cooldown = EnemyType1.ANIMATION_COOLDOWN
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.x = random.randint(20, screen_width - 20)
        self._x_speed = random.uniform(-0.8, 0.8)

    def update_animation(self, sprites):
        current_time = pygame.time.get_ticks()

        if current_time - self._last_frame_time > self._animation_cooldown:
            self._last_frame_time = pygame.time.get_ticks()

            self._animation_count += 1

            if self._animation_count >= len(self.sprites):
                self._animation_count = 0

            self.image = sprites[self._animation_count]

    def moviment(self):
        self.rect.x += self._x_speed

        if self.rect.left <= 0 or self.rect.right >= 800:
            self._x_speed *= -1

class EnemyType2(Enemy):

    ANIMATION_COOLDOWN = 70

    def __init__(self, screen_width, screen_height, default_image):
        super().__init__(screen_width, screen_height)
        self.image = default_image
        self._animation_count = 0
        self._last_frame_time = 0 
        self._animation_cooldown = EnemyType2.ANIMATION_COOLDOWN
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.x = random.randint(20, screen_width - 20)
        self._speed = random.uniform(1.7, 1.8)
        self._x_speed = random.uniform(-2, 2)
        self._stay_y = random.randint(100, 300)

    def update_animation(self, sprites, sprites_turn):
        current_time = pygame.time.get_ticks()

        if self._x_speed == 0:

            if current_time - self._last_frame_time > self._animation_cooldown:
                self._last_frame_time = pygame.time.get_ticks()
                self._animation_count += 1

                if self._animation_count >= len(self.sprites):
                    self._animation_count = 0

                self.image = sprites[self._animation_count]

        elif self._x_speed < 0:

            if current_time - self._last_frame_time > self._animation_cooldown:
                self._last_frame_time = pygame.time.get_ticks()
                self._animation_count += 1

                if self._animation_count >= len(self.sprites_turn):
                    self._animation_count = 0

                flippled_turn = pygame.transform.flip(sprites_turn[self._animation_count], True, False)

                self.image = flippled_turn

        elif self._x_speed > 0:

            if current_time - self._last_frame_time > self._animation_cooldown:
                self._last_frame_time = pygame.time.get_ticks()
                self._animation_count += 1

                if self._animation_count >= len(self.sprites_turn):
                    self._animation_count = 0

                self.image = self.sprites_turn[self._animation_count]

    def moviment(self):
        if self.rect.y >= self._stay_y:
            self._speed = 0
            self._x_speed = 0
        else:
            self.rect.x += self._x_speed

            if self.rect.left <= 0 or self.rect.right >= 800:
                self._x_speed *= -1


class FairyType1(EnemyType2):
    sprites = [
            pygame.image.load("assets/images/enemies/fairy1_0.png"), 
            pygame.image.load("assets/images/enemies/fairy1_1.png"), 
            pygame.image.load("assets/images/enemies/fairy1_2.png"), 
            pygame.image.load("assets/images/enemies/fairy1_3.png")
            ]

    sprites_turn =  [
            pygame.image.load("assets/images/enemies/turn1_0.png"), 
            pygame.image.load("assets/images/enemies/turn1_1.png"), 
            pygame.image.load("assets/images/enemies/turn1_2.png"), 
            pygame.image.load("assets/images/enemies/turn1_3.png")
            ]
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, self.sprites[0])
    
    def update(self):
        super().update()
        self.update_animation(self.sprites, self.sprites_turn)
        self.moviment()

class FairyType2(EnemyType2):
    sprites = [
            pygame.image.load("assets/images/enemies/fairy2_0.png"), 
            pygame.image.load("assets/images/enemies/fairy2_1.png"), 
            pygame.image.load("assets/images/enemies/fairy2_2.png"), 
            pygame.image.load("assets/images/enemies/fairy2_3.png")
            ]

    sprites_turn =  [
            pygame.image.load("assets/images/enemies/turn2_0.png"), 
            pygame.image.load("assets/images/enemies/turn2_1.png"), 
            pygame.image.load("assets/images/enemies/turn2_2.png"), 
            pygame.image.load("assets/images/enemies/turn2_3.png")
            ]
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, self.sprites[0])
    
    def update(self):
        super().update()
        self.update_animation(self.sprites, self.sprites_turn)
        self.moviment()

class FairyType3(EnemyType2):
    sprites = [
            pygame.image.load("assets/images/enemies/fairy3_0.png"), 
            pygame.image.load("assets/images/enemies/fairy3_1.png"), 
            pygame.image.load("assets/images/enemies/fairy3_2.png"), 
            pygame.image.load("assets/images/enemies/fairy3_3.png")
            ]

    sprites_turn =  [
            pygame.image.load("assets/images/enemies/turn3_0.png"), 
            pygame.image.load("assets/images/enemies/turn3_1.png"), 
            pygame.image.load("assets/images/enemies/turn3_2.png"), 
            pygame.image.load("assets/images/enemies/turn3_3.png")
            ]
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, self.sprites[0])
    
    def update(self):
        super().update()
        self.update_animation(self.sprites, self.sprites_turn)
        self.moviment()

class FairyType4(EnemyType1):
    sprites = [
            pygame.image.load("assets/images/enemies/fairy4_0.png"), 
            pygame.image.load("assets/images/enemies/fairy4_1.png"), 
            pygame.image.load("assets/images/enemies/fairy4_2.png"), 
            pygame.image.load("assets/images/enemies/fairy4_3.png")
            ]
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, self.sprites[0])

    def update(self):
        super().update()
        self.update_animation(self.sprites)
        self.moviment()

class FairyType5(EnemyType1):
    sprites = [
            pygame.image.load("assets/images/enemies/fairy5_0.png"), 
            pygame.image.load("assets/images/enemies/fairy5_1.png"), 
            pygame.image.load("assets/images/enemies/fairy5_2.png"), 
            pygame.image.load("assets/images/enemies/fairy5_3.png")
            ]
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, self.sprites[0])

    def update(self):
        super().update()
        self.update_animation(self.sprites)
        self.moviment()