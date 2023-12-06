import pygame

from classes.player import Player
from classes.background import Background
from classes.enemies import *
from classes.spawner import Spawn

class Game:
    def __init__(self):
        # Inicializa o jogo
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        # Cria o background e adiciona ao grupo de todos os sprites
        self.background = Background((800, 600), -7768, 1, 'assets/images/background/starfield.png')

        # Cria o jogador e adiciona ao grupo de todos os sprites
        self.player = Player()

        self.all_enemies = pygame.sprite.Group()

        self.spawn_manager = Spawn(self.all_enemies)

        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
    
    def handle_collision(self):
        for bullet in self.player_bullets:
            for enemy in self.all_enemies:
                if enemy.hitbox.colliderect(bullet.hitbox):
                    enemy.get_hit()
                    bullet.kill()
        
        for bullet in self.enemy_bullets:
            if self.player.hitbox.colliderect(bullet.hitbox):
                self.player.get_hit()
                bullet.kill()

    def run(self):
        # Loop principal do jogo
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Surgimento dos inimigos
            self.spawn_manager.spawn()

            for enemy in self.all_enemies:
                if enemy.can_shoot():
                    bullets = enemy.spawn_bullets()
                    self.enemy_bullets.add(bullets)
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.player.can_shoot():
                bullets = self.player.spawn_bullets()
                self.player_bullets.add(bullets)
            
            self.all_sprites = pygame.sprite.Group()
            self.all_sprites.add(self.background, self.player, self.all_enemies, self.player_bullets, self.enemy_bullets)

            # Atualiza os sprites
            self.all_sprites.update()

            # Desenha os sprites na tela
            self.all_sprites.draw(self.screen)

            self.handle_collision()

            if self.player.life <= 0:
                running = False

            # Atualiza a tela
            pygame.display.flip()
            self.clock.tick(50)