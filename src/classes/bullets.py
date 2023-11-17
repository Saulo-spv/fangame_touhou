import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, speed, degrees, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.midbottom = (pos[0]+10, pos[1]+10)

        self.max_x = pygame.display.get_surface().get_width()
        self.max_y = pygame.display.get_surface().get_height()

        self.speed = speed
        self.degrees = degrees

        self.dx = math.cos(math.radians(self.degrees)) * self.speed
        self.dy = -(math.sin(math.radians(self.degrees)) * self.speed)

    def move(self):
        # Movimenta o tiro
        self.rect.y -= self.dy
        self.rect.x += self.dx

    def destroy(self):
        # Remove o tiro quando atinge as bordas da tela
        if self.rect.bottom < 0 or self.rect.top > self.max_y or self.rect.left < 0 or self.rect.right > self.max_x:
            self.kill()

    def update(self):
        self.move()
        self.destroy()


class PlayerBullet(Bullet):
    def __init__(self, pos, image):
        # Inicializa e posiciona o tiro
        super().__init__(pos, 5, -90, image)


class EnemyBullet1(Bullet):
    def __init__(self, pos, degrees):
        image = pygame.image.load('assets/images/enemies/bullet0.png')

        super().__init__(pos, 2, degrees, image)


class EnemyBullet2(Bullet):
    def __init__(self, pos, degrees):
        image = pygame.image.load('assets/images/enemies/bullet1.png')

        super().__init__(pos, 2, degrees, image)


class EnemyBullet3(Bullet):
    def __init__(self, pos, degrees):
        image = pygame.image.load('assets/images/enemies/bullet2.png')

        super().__init__(pos, 2, degrees, image)


class EnemyBullet4(Bullet):
    def __init__(self, pos, degrees):
        image = pygame.image.load('assets/images/enemies/bullet3.png')

        super().__init__(pos, 2, degrees, image)


class EnemyBullet5(Bullet):
    def __init__(self, pos, degrees):
        image = pygame.image.load('assets/images/enemies/bullet4.png')

        super().__init__(pos, 2, degrees, image)