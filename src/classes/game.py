import pygame
from classes.player import Player
from classes.background import Background
from classes.enemies import *
from classes.button import Button

class Game:
    def __init__(self):
        # Inicializa o jogo
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Touhou")
        self.clock = pygame.time.Clock()

        # Cria o background e adiciona ao grupo de todos os sprites
        self.background = Background((800, 600), -7768, 1, 'assets/images/background/starfield.png')

        # Cria o jogador e adiciona ao grupo de todos os sprites
        self.player = Player()

        self.all_enemies = pygame.sprite.Group()
        self.all_enemies.add([
            BigFairyType1(),
            BigFairyType2(),
            BigFairyType3(),
            SmallFairy(1),
            SmallFairy(2)
        ])

        self.all_bullets = pygame.sprite.Group()

        # Variaveis do Menu de Pause
        self.paused = False
        self.botao_continue = Button(300, 200, 200, 50, "Continue", font_size=30)
        self.botao_quit = Button(300, 300, 200, 50, "Quit", font_size=30)

    def run(self):
        # Loop principal do jogo
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused

            if not self.paused:
                self.update_game()
            else:
                # Atualiza a Tela de Pause e Desenha os Botões
                self.paused_screen()
                self.botao_continue.draw(self.screen)
                self.botao_quit.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)


    # Atualiza o Jogo
    def update_game(self):
        for enemy in self.all_enemies:
            if enemy.can_shoot():
                bullets = enemy.spawn_bullets()
                self.all_bullets.add(bullets)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.player.can_shoot():
            bullets = self.player.spawn_bullets()
            self.all_bullets.add(bullets)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.background, self.player, self.all_enemies, self.all_bullets)

        self.all_sprites.update()
        self.all_sprites.draw(self.screen)

    # Atualiza a tela de Pause
    def paused_screen(self):
        
        # Atualiza os Botões
        self.botao_continue.update()
        self.botao_quit.update()

        # Verifica Eventos
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.botao_continue.rect.collidepoint(mouse_pos):
                self.paused = False
            elif self.botao_quit.rect.collidepoint(mouse_pos):
                pygame.quit()
                quit()