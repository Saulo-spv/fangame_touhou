import pygame
import random

from classes.bullets import *


class Enemy(pygame.sprite.Sprite):
    '''Classe abstrata base dos inimigos'''

    def __init__(self, all_sprites, bullets, shoot_cooldown):
        super().__init__()

        self.speed = random.uniform(0.8, 0.9)

        self.screen_height = pygame.display.get_surface().get_height()
        self.screen_width = pygame.display.get_surface().get_width()

        self.all_sprites = all_sprites
        self.bullets = bullets

        self.last_shoot_time = 0
        self.shoot_cooldown = shoot_cooldown
    
    def can_shoot(self):
        # Verifica se o tempo desde o último tiro é maior que o cooldown
        now = pygame.time.get_ticks()
        
        return now - self.last_shoot_time > self.shoot_cooldown

    def update(self):
        self.rect.y += self._speed

        if self.rect.top >= 600:
            self.kill()


class EnemyType1(Enemy):

    ANIMATION_COOLDOWN = 70

    def __init__(self, all_sprites, bullets, default_image, shoot_cooldown):
        super().__init__(all_sprites, bullets, shoot_cooldown)
        self.image = default_image
        self._animation_count = 0
        self._last_frame_time = 0 
        self._animation_cooldown = EnemyType1.ANIMATION_COOLDOWN
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.x = random.randint(20, self.screen_width - 20)
        self._x_speed = random.uniform(-0.8, 0.8)

    def update_animation(self, sprites):
        current_time = pygame.time.get_ticks()

        if current_time - self._last_frame_time > self._animation_cooldown:
            self._last_frame_time = pygame.time.get_ticks()

            self._animation_count += 1

            if self._animation_count >= len(self.sprites):
                self._animation_count = 0

            self.image = sprites[self._animation_count]

    def move(self):
        self.rect.x += self._x_speed

        if self.rect.left <= 0 or self.rect.right >= 800:
            self._x_speed *= -1


class EnemyType2(Enemy):

    ANIMATION_COOLDOWN = 70

    def __init__(self, all_sprites, bullets, default_image, shoot_cooldown):
        super().__init__(all_sprites, bullets, shoot_cooldown)
        self.image = default_image
        self._animation_count = 0
        self._last_frame_time = 0 
        self._animation_cooldown = EnemyType2.ANIMATION_COOLDOWN
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.x = random.randint(20, self.screen_width - 20)
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

    def move(self):
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
    
    def __init__(self, all_sprites, bullets):
        super().__init__(all_sprites, bullets, self.sprites[0], 1500)
    
    def fire_bullet(self):
        # Cria os novos tiros e os adicionam ao grupo de sprites
        bullets = [
            EnemyBullet1((self.rect.centerx, self.rect.centery), 0),
            EnemyBullet1((self.rect.centerx, self.rect.centery), 90),
            EnemyBullet1((self.rect.centerx, self.rect.centery), 180),
            EnemyBullet1((self.rect.centerx, self.rect.centery), 270),
        ]

        self.all_sprites.add(bullets)
        self.bullets.add(bullets)

        self.last_shoot_time = pygame.time.get_ticks()
    
    def update(self):
        super().update()
        self.update_animation(self.sprites, self.sprites_turn)
        self.move()

        # Atira se conseguir
        if self.can_shoot():
            self.fire_bullet()


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
    
    def __init__(self, all_sprites, bullets):
        super().__init__(all_sprites, bullets, self.sprites[0], 1500)

    def fire_bullet(self):
        # Cria os novos tiros e os adicionam ao grupo de sprites
        bullets = [
            EnemyBullet2((self.rect.centerx, self.rect.top + 10), 30),
            EnemyBullet2((self.rect.centerx, self.rect.top + 10), 60),
            EnemyBullet2((self.rect.centerx, self.rect.top + 10), 90),
            EnemyBullet2((self.rect.centerx, self.rect.top + 10), 120),
            EnemyBullet2((self.rect.centerx, self.rect.top + 10), 150),
        ]

        self.all_sprites.add(bullets)
        self.bullets.add(bullets)

        self.last_shoot_time = pygame.time.get_ticks()
    
    def update(self):
        super().update()
        self.update_animation(self.sprites, self.sprites_turn)
        self.move()

        # Atira se conseguir
        if self.can_shoot():
            self.fire_bullet()

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

    def __init__(self, all_sprites, bullets):
        super().__init__(all_sprites, bullets, self.sprites[0], 400)

        self.bullet_direction = 0
    
    def fire_bullet(self):
        # Calcula a direção do tiro
        degrees = self.bullet_direction * 20
        self.bullet_direction = (self.bullet_direction + 1) % 10

        # Cria um novo tiro e o adiciona ao grupo de sprites
        bullet = EnemyBullet3((self.rect.centerx, self.rect.top), degrees)

        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

        self.last_shoot_time = pygame.time.get_ticks()
    
    def update(self):
        super().update()
        self.update_animation(self.sprites, self.sprites_turn)
        self.move()

        # Atira se conseguir
        if self.can_shoot():
            self.fire_bullet()


class FairyType4(EnemyType1):
    sprites = [
        pygame.image.load("assets/images/enemies/fairy4_0.png"), 
        pygame.image.load("assets/images/enemies/fairy4_1.png"), 
        pygame.image.load("assets/images/enemies/fairy4_2.png"), 
        pygame.image.load("assets/images/enemies/fairy4_3.png")
    ]

    def __init__(self, all_sprites, bullets):
        super().__init__(all_sprites, bullets, self.sprites[0], 800)
    
    def fire_bullet(self):
        # Calcula a direção do tiro
        degrees = random.randint(0, 180)

        # Cria um novo tiro e o adiciona ao grupo de sprites
        bullet = EnemyBullet4((self.rect.centerx, self.rect.top), degrees)

        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

        self.last_shoot_time = pygame.time.get_ticks()

    def update(self):
        super().update()
        self.update_animation(self.sprites)
        self.move()

        # Atira se conseguir
        if self.can_shoot():
            self.fire_bullet()


class FairyType5(EnemyType1):
    sprites = [
        pygame.image.load("assets/images/enemies/fairy5_0.png"), 
        pygame.image.load("assets/images/enemies/fairy5_1.png"), 
        pygame.image.load("assets/images/enemies/fairy5_2.png"), 
        pygame.image.load("assets/images/enemies/fairy5_3.png")
    ]

    def __init__(self, all_sprites, bullets):
        super().__init__(all_sprites, bullets, self.sprites[0], 800)
    
    def fire_bullet(self):
        # Calcula a direção do tiro
        degrees = random.randint(0, 180)

        # Cria um novo tiro e o adiciona ao grupo de sprites
        bullet = EnemyBullet5((self.rect.centerx, self.rect.top), degrees)

        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

        self.last_shoot_time = pygame.time.get_ticks()
    
    def update(self):
        super().update()
        self.update_animation(self.sprites)
        self.move()

        # Atira se conseguir
        if self.can_shoot():
            self.fire_bullet()