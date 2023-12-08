import pygame

from classes.player import Player
from classes.background import Background
from classes.enemies import *
from classes.button import Button
from classes.spawner import Spawn
from classes.menu import Menu


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Touhou")
        self.clock = pygame.time.Clock()

        self.background = Background((800, 600), -7768, 1, 'assets/images/background/starfield.png')

        self.life_heart = pygame.image.load('assets/images/interface/heart.png').subsurface(0, 0, 16, 16).convert_alpha()
        self.life_heart = pygame.transform.scale(self.life_heart, (30, 30))

        self.font = pygame.font.Font('assets/fonts/Silkscreen-Regular.ttf', 20)

        self.player = Player()

        self.all_enemies = pygame.sprite.Group()

        self.spawn_manager = Spawn(self.all_enemies)

        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()

        try:
            data = open('highscore.txt', 'r')
            self.__highscore = int(data.read())
            data.close()
        except IOError and ValueError:
            self.__highscore = 0

        self.__score = 0
        
        self.paused = False
        self.botao_continue = Button(300, 200, 200, 50, "Continue", font_size=30)
        self.botao_quit = Button(300, 300, 200, 50, "Quit", font_size=30)
        self.botao_again = Button(300, 200, 200, 50, "Again", font_size=30)
        self.botao_menu = Button(300, 400, 200, 50, "Return to Menu", font_size=30)
    
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        self.__score = value
    
    @property
    def highscore(self):
        return self.__highscore
    
    @highscore.setter
    def highscore(self, value):
        self.__highscore = value
    
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
    
    def update_interface(self):
        heart_x_pos = 40
        for i in range(self.player.life):
            self.screen.blit(self.life_heart, (10 + heart_x_pos, 20))
            heart_x_pos += 40
        
        score_label = self.font.render(f'SCORE: {self.score}', 1, (255, 0, 0))
        self.screen.blit(score_label, (550,15))

        highscore_label = self.font.render(f'HIGHSCORE: {self.highscore}', 1, (255, 0, 0))
        self.screen.blit(highscore_label, (550,40))
    
    def update_score(self):
        self.score += 2

        if self.score >= self.highscore:
            self.highscore = self.score
    
    def update_highscore(self):
        if self.highscore == self.score:
            data = open('highscore.txt', 'w')
            data.write(str(self.highscore))
            data.close()
    
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

            if self.player.life <= 0:
                self.game_over()
                self.botao_again.draw(self.screen)
                self.botao_quit.draw(self.screen)
                self.botao_menu.draw(self.screen)
                self.update_highscore()
            elif not self.paused:
                self.update_game()
            else:
                # Atualiza a Tela de Pause e Desenha os Botões
                self.paused_screen()
                self.botao_continue.draw(self.screen)
                self.botao_menu.draw(self.screen)
                self.botao_quit.draw(self.screen)
            
            pygame.display.flip()

    # Atualiza o Jogo
    def update_game(self):
        # Surgimento dos inimigos
        self.spawn_manager.spawn()
        
        for enemy in self.all_enemies:
            if enemy.can_shoot():
                bullets = enemy.spawn_bullets()
                self.enemy_bullets.add(bullets)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_j] and self.player.can_shoot():
            bullets = self.player.spawn_bullets()
            self.player_bullets.add(bullets)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.background, self.player, self.all_enemies, self.enemy_bullets, self.player_bullets)

        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        
        self.handle_collision()

        self.update_score()

        self.update_interface()

        self.clock.tick(50)

    def paused_screen(self):
        # Atualiza os Botões
        self.botao_continue.update()
        self.botao_quit.update()
        self.botao_menu.update()

        # Verifica Eventos
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.botao_continue.rect.collidepoint(mouse_pos):
                self.paused = False
            elif self.botao_quit.rect.collidepoint(mouse_pos):
                pygame.quit()
                quit()
            elif self.botao_menu.rect.collidepoint(mouse_pos):
                    menu = Menu()
                    menu.run_menu()
                    self.reset_game()   

    def game_over(self):

        # Escreve Game Over
        game_over_text = self.font.render("Game Over", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 5))
        self.screen.blit(game_over_text, text_rect)

        # Atualiza os Botões
        self.botao_again.update()
        self.botao_quit.update()
        self.botao_menu.update()

        # Verifica Eventos
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if mouse_pressed:
            mouse_pos = pygame.mouse.get_pos()
            if self.botao_again.rect.collidepoint(mouse_pos):
                self.reset_game()
            elif self.botao_quit.rect.collidepoint(mouse_pos):
                pygame.quit()
                quit()
            elif self.botao_menu.rect.collidepoint(mouse_pos):
                    menu = Menu()
                    menu.run_menu()
                    self.reset_game()

            # Atualiza a tela
            pygame.display.flip()
            self.clock.tick(50)

    def reset_game(self):
        # Reinicia a pontuação
        self.score = 0

        # Reposiciona o jogador no lugar de início
        self.player.rect.x = 400
        self.player.rect.y = 550

        # Reinicia a vida do jogador
        self.player.life = 3

        # Limpa os grupos de sprites
        self.all_enemies.empty()
        self.player_bullets.empty()
        self.enemy_bullets.empty()

        # Volta para o loop principal do jogo
        self.run()