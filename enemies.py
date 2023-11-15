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
    sprites = [
            pygame.image.load("fairies/fairy4_0.png"), 
            pygame.image.load("fairies/fairy4_1.png"), 
            pygame.image.load("fairies/fairy4_2.png"), 
            pygame.image.load("fairies/fairy4_3.png")
            ]

    ANIMATION_COOLDOWN = 70

    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.image = EnemyType1.sprites[0]
        self._animation_count = 0
        self._last_frame_time = 0 
        self._animation_cooldown = EnemyType1.ANIMATION_COOLDOWN
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, screen_width - 20)
        self._x_speed = random.uniform(-0.8, 0.8)

    def update(self):
        super().update()

        EnemyType1.update_animation(self)
        EnemyType1.moviment(self)

    def update_animation(self):
        current_time = pygame.time.get_ticks()

        if current_time - self._last_frame_time > self._animation_cooldown:
            self._last_frame_time = pygame.time.get_ticks()

            self._animation_count += 1

            if self._animation_count >= len(self.sprites):
                self._animation_count = 0

            self.image = self.sprites[self._animation_count]

    def moviment(self):
        self.rect.x += self._x_speed

        if self.rect.left <= 0 or self.rect.right >= 800:
            self._x_speed *= -1

class EnemyType2(Enemy):
    sprites = [
            pygame.image.load("fairies/fairy1_0.png"), 
            pygame.image.load("fairies/fairy1_1.png"), 
            pygame.image.load("fairies/fairy1_2.png"), 
            pygame.image.load("fairies/fairy1_3.png")
            ]

    sprites_turn =  [
            pygame.image.load("fairies/turn1_0.png"), 
            pygame.image.load("fairies/turn1_1.png"), 
            pygame.image.load("fairies/turn1_2.png"), 
            pygame.image.load("fairies/turn1_3.png")
            ]

    ANIMATION_COOLDOWN = 70

    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.image = EnemyType2.sprites[0]
        self._animation_count = 0
        self._last_frame_time = 0 
        self._animation_cooldown = EnemyType2.ANIMATION_COOLDOWN
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, screen_width - 20)
        self._speed = random.uniform(1.7, 1.8)
        self._x_speed = random.uniform(-2, 2)
        self._stay_y = random.randint(100, 300)

    def update(self):
        super().update()

        EnemyType2.update_animation(self)
        EnemyType2.moviment(self)

    def update_animation(self):
        current_time = pygame.time.get_ticks()

        if self._x_speed == 0:

            if current_time - self._last_frame_time > self._animation_cooldown:
                self._last_frame_time = pygame.time.get_ticks()
                self._animation_count += 1

                if self._animation_count >= len(self.sprites):
                    self._animation_count = 0

                self.image = self.sprites[self._animation_count]

        elif self._x_speed < 0:

            if current_time - self._last_frame_time > self._animation_cooldown:
                self._last_frame_time = pygame.time.get_ticks()
                self._animation_count += 1

                if self._animation_count >= len(self.sprites_turn):
                    self._animation_count = 0

                flippled_turn = pygame.transform.flip(self.sprites_turn[self._animation_count], True, False)

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