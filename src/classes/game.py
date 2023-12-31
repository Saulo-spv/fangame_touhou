"""Classe Game

Módulo responsável por implementar a classe Game, que representa o jogo.

"""
import pygame
import sys

from classes.player import Player
from classes.background import Background
from classes.enemies import *
from classes.button import Button
from classes.spawner import Spawn
from classes.music_player import Music
from classes.effects import Effect
from classes.power_up import PowerUp


class Game:
    def __init__(self):
        """Inicializa uma nova instância da classe Game.
        """
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Touhou")

        # Inicializa o Relógio
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.last_time_pause = 0

        self.music_player = Music()

        self.player = Player()

        self.all_enemies = pygame.sprite.Group()
        self.spawn_manager = Spawn(self.all_enemies)

        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()

        self.all_power_ups = pygame.sprite.Group()

        self.all_effects = pygame.sprite.Group()

        # Carrega a pontuação máxima
        try:
            data = open('highscore.txt', 'r')
            self.highscore = int(data.read())
            data.close()
        except IOError and ValueError:
            self.highscore = 0

        self.score = 0
        
        self.paused = False
        self.start_game = False

        self.load_assets()
    
    @property
    def score(self) -> int:
        """Obtém a pontuação atual.

        Returns
        -------
        int
            A pontuação atual.
        """
        return self.__score
    
    @score.setter
    def score(self, value: int):
        """Define a pontuação atual.

        Parameters
        ----------
        value : int
            A nova pontuação atual.
        """
        self.__score = value
    
    @property
    def highscore(self) -> int:
        """Obtém a pontuação máxima.

        Returns
        -------
        int
            A pontuação máxima.
        """
        return self.__highscore
    
    @highscore.setter
    def highscore(self, value: int):
        """Define a pontuação máxima.

        Parameters
        ----------
        value : int
            A nova pontuação máxima.
        """
        self.__highscore = value
    
    def load_assets(self):
        """Carrega os assets do jogo.
        """
        # Carrega o background
        self.menu_background = pygame.image.load('assets/images/background/main_menu.png').convert_alpha()
        self.menu_background = pygame.transform.scale(self.menu_background, (800, 600))
        self.credits_background = pygame.image.load('assets/images/background/credits.png').convert_alpha()
        self.credits_background = pygame.transform.scale(self.credits_background, (800, 600))
        self.game_background = Background((800, 600), -7768, 1, 'assets/images/background/starfield.png')

        # Carrega os sprites da interface
        self.life_heart = pygame.image.load('assets/images/interface/heart.png').subsurface(0, 0, 16, 16).convert_alpha()
        self.life_heart = pygame.transform.scale(self.life_heart, (30, 30))
        self.shield_image = pygame.image.load('assets/images/power_ups/shield.png').convert_alpha()
        self.shield_image = pygame.transform.scale(self.shield_image, (30, 30))

        # Carrega os sons
        self.player_bullet_sound = pygame.mixer.Sound('assets/sound/effects/attack.wav')

        self.font = pygame.font.Font('assets/fonts/Silkscreen-Regular.ttf', 20)

        # Carrega os botões
        self.main_menu_play_button = Button(105, 200, 150, 50, font_size=30 ,text="PLAY")
        self.main_menu_credits_button = Button(105, 300, 150, 50, font_size=30, text="CREDITS")
        self.main_menu_quit_button = Button(105, 400, 150, 50, font_size=30, text="QUIT")
        self.pause_screen_continue_button = Button(300, 200, 200, 50, font_size=30, text= "Continue")
        self.pause_screen_quit_button = Button(300, 300, 200, 50, font_size=30, text="Quit")
        self.pause_screen_again_button = Button(300, 200, 200, 50, font_size=30, text="Again")
        self.pause_screen_menu_button = Button(300, 400, 200, 50, font_size=30, text="Return to Menu")
    
    def handle_collision(self):
        """Verifica as colisões entre os sprites.
        """
        for bullet in self.player_bullets:
            for enemy in self.all_enemies:
                if enemy.hitbox.colliderect(bullet.hitbox):
                    if enemy.life == 1:
                        # Cria o efeito de explosão
                        if isinstance(enemy, SmallFairy):
                            self.all_effects.add(Effect((enemy.rect.centerx, enemy.rect.centery+10), 'explosion_1'))
                        elif (enemy, BigFairy):
                            self.all_effects.add(Effect((enemy.rect.centerx, enemy.rect.centery+10), 'explosion_2'))
                        
                        # Dropa o power-up
                        power_up = enemy.drop_power_up()
                        if power_up is not None:
                            self.all_power_ups.add(PowerUp((enemy.rect.centerx, enemy.rect.centery+10), power_up, self.player, self.enemy_bullets))
                    
                    enemy.get_hit()
                    bullet.kill()
        
        for bullet in self.enemy_bullets:
            if self.player.hitbox.colliderect(bullet.hitbox):
                # Verifica se o jogador está com o escudo
                if self.player.shield:
                    self.player.shield = False
                else:
                    self.player.get_hit()
                
                bullet.kill()
        
        for power_up in self.all_power_ups:
            # Verifica se o jogador coletou o power-up
            if self.player.hitbox.colliderect(power_up.hitbox):
                power_up.collect()
    
    def update_interface(self):
        """Atualiza a interface do jogo.
        """
        heart_x_pos = 40
        for i in range(self.player.life):
            self.screen.blit(self.life_heart, (10 + heart_x_pos, 20))
            heart_x_pos += 40
        
        if self.player.shield:
            self.screen.blit(self.shield_image, (10 + heart_x_pos, 20))
        
        score_label = self.font.render(f'SCORE: {self.score}', 1, (255, 0, 0))
        self.screen.blit(score_label, (550,15))

        highscore_label = self.font.render(f'HIGHSCORE: {self.highscore}', 1, (255, 0, 0))
        self.screen.blit(highscore_label, (550,40))
    
    def update_score(self):
        """Atualiza a pontuação do jogo.
        """
        self.score += 2

        if self.score >= self.highscore:
            self.highscore = self.score
    
    def update_highscore(self):
        """Atualiza a pontuação máxima do jogo.
        """
        if self.highscore == self.score:
            data = open('highscore.txt', 'w')
            data.write(str(self.highscore))
            data.close()
    
    def run(self):
        """Executa o jogo.
        """
        # Loop principal do jogo
        running = True
        while running:
            # Atualiza o tempo
            current_ticks = pygame.time.get_ticks()

            # Atualiza a música
            self.music_player.play_music()
            self.music_player.current_ticks = current_ticks

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused
                        self.last_time_pause = pygame.time.get_ticks()
                        self.music_player.pause_music()

            # Verifica se o jogador perdeu
            if self.player.life <= 0:
                self.last_time_pause = current_ticks

                self.game_over()

                self.pause_screen_again_button.draw(self.screen)
                self.pause_screen_quit_button.draw(self.screen)
                self.pause_screen_menu_button.draw(self.screen)
                
                self.update_highscore()
            elif not self.paused:
                self.current_time += current_ticks - self.last_time_pause
                self.last_time_pause = current_ticks
                
                self.update_game()
            else:
                # Atualiza a Tela de Pause e Desenha os Botões
                self.paused_screen()

                self.pause_screen_continue_button.draw(self.screen)
                self.pause_screen_menu_button.draw(self.screen)
                self.pause_screen_quit_button.draw(self.screen)

                self.music_player.music_select()
            
            pygame.display.flip()

    # Atualiza o Jogo
    def update_game(self):
        """Atualiza o jogo.
        """
        # Surgimento dos inimigos
        self.spawn_manager.current_time = self.current_time
        self.spawn_manager.spawn()
        
        # Realiza os disparos dos inimigos
        for enemy in self.all_enemies:
            if enemy.can_shoot():
                bullets = enemy.spawn_bullets()
                self.enemy_bullets.add(bullets)

        # Realiza os disparos do jogador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j] and self.player.can_shoot():
            self.player_bullet_sound.play()
            bullets = self.player.spawn_bullets()
            self.player_bullets.add(bullets)

        # Cria grupo com todos os sprites
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.game_background, self.player, self.all_enemies, self.enemy_bullets,
                             self.player_bullets, self.all_power_ups, self.all_effects)

        # Atualiza os sprites
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        
        self.handle_collision()

        self.update_score()

        self.update_interface()

        self.clock.tick(50)

    def paused_screen(self):
        """Atualiza a tela de pause.
        """
        # Atualiza os Botões
        self.pause_screen_continue_button.update()
        self.pause_screen_quit_button.update()
        self.pause_screen_menu_button.update()

        # Verifica Eventos
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.pause_screen_continue_button.rect.collidepoint(mouse_pos):
                self.paused = False
                self.music_player.pause_music()
            elif self.pause_screen_quit_button.rect.collidepoint(mouse_pos):
                pygame.quit()
                quit()
            elif self.pause_screen_menu_button.rect.collidepoint(mouse_pos):
                self.main_menu()
                self.reset_game()
                self.run()

    def game_over(self):
        """Atualiza a tela de Game Over.
        """
        pygame.mixer.music.stop()

        # Escreve Game Over
        game_over_text = self.font.render("Game Over", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 5))
        self.screen.blit(game_over_text, text_rect)

        # Atualiza os Botões
        self.pause_screen_again_button.update()
        self.pause_screen_quit_button.update()
        self.pause_screen_menu_button.update()

        # Verifica Eventos
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if mouse_pressed:
            mouse_pos = pygame.mouse.get_pos()
            if self.pause_screen_again_button.rect.collidepoint(mouse_pos):
                self.reset_game()
                self.run()
            elif self.pause_screen_quit_button.rect.collidepoint(mouse_pos):
                pygame.quit()
                quit()
            elif self.pause_screen_menu_button.rect.collidepoint(mouse_pos):
                self.main_menu()
                self.reset_game()
                self.run()

            # Atualiza a tela
            pygame.display.flip()
            self.clock.tick(40)

    def reset_game(self):
        """Reinicia o jogo.
        """
        # Reinicia a pontuação
        self.score = 0

        # Reposiciona o jogador no lugar de início
        self.player.rect.x = 400
        self.player.rect.y = 550

        # Reinicia a vida do jogador
        self.player.life = 3

        # Reinicia o tempo
        self.current_time = 0

        # Limpa os grupos de sprites
        self.all_enemies.empty()
        self.player_bullets.empty()
        self.enemy_bullets.empty()
        self.all_power_ups.empty()
        self.all_effects.empty()

        # Reinicia o spawn
        self.spawn_manager.reset()

        # Reinicia a música
        self.music_player.music_play = False
        self.music_player.music_pause = False

        self.paused = False
    
    def main_menu(self):
        """Atualiza a tela de menu principal.
        """
        self.reset_game()

        while not self.start_game:
            self.screen.blit(self.menu_background, (0, 0))
            
            menu_text = pygame.font.Font(None, 100).render("MAIN MENU", True, "#b68f40")
            menu_rect = menu_text.get_rect(center=(400, 100))
            self.screen.blit(menu_text, menu_rect)

            # Desenha e Atualiza os botões
            self.main_menu_play_button.draw(self.screen)
            self.main_menu_credits_button.draw(self.screen)
            self.main_menu_quit_button.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.main_menu_play_button.rect.collidepoint(event.pos):
                        self.run()
                    elif self.main_menu_credits_button.rect.collidepoint(event.pos):
                        self.credits()
                    elif self.main_menu_quit_button.rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
    
    def credits(self):
        """Atualiza a tela de créditos.
        """
        while True:
            mouse_pos = pygame.mouse.get_pos()

            self.screen.blit(self.credits_background, (0, 0))

            title = pygame.font.Font(None, 100).render("CREDITS", True, "#b68f40")
            name_1 = pygame.font.Font(None, 40).render("YURE OLIVEIRA", True, "#b68f40")
            name_2 = pygame.font.Font(None, 40).render("SAULO PIRES", True, "#b68f40")
            name_3 = pygame.font.Font(None, 40).render("GABRIEL MATOS", True, "#b68f40")

            title_rect = title.get_rect(center=(620, 100))
            name_1_rect = name_1.get_rect(center=(620, 250))
            name_2_rect = name_2.get_rect(center=(620, 300))
            name_3_rect = name_3.get_rect(center=(620, 350))

            self.screen.blit(title, title_rect)
            self.screen.blit(name_1, name_1_rect)
            self.screen.blit(name_2, name_2_rect)
            self.screen.blit(name_3, name_3_rect)

            # Cria Botão Para Voltar
            credits_back = Button(x=550, y=500, width=200, height=50, text="BACK")
            credits_back.update()
            credits_back.draw(self.screen)

            # Verifica Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if credits_back.rect.collidepoint(mouse_pos):
                        return

            pygame.display.update()