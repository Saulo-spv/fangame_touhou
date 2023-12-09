"""Classe Music

Módulo responsável por implementar a classe Music, que representa o player de música do jogo.

"""
import pygame


class Music:
    def __init__(self):
        """Inicializa uma nova instância da classe Music.
        """
        # Variavéis de controle
        self.music_play = False
        self.music_pause = False
        self.music_change = False

        # Variavéis auxiliares
        self.actual_music = 0
        self.last_change = 0
        self.current_ticks = 0

        # Lista das músicas disponíveis
        self.music_list = [
            'Remilia Scarlet\'s Theme - Septette for the Dead Princess',
            'Yukari\'s Theme - Necrofantasia',
            'Secret God Matara ~ Hidden Star in All Seasons',
        ]

    def play_music(self):
        """Toca a música.
        """
        # Inicialização da música
        if not self.music_play:
            pygame.mixer.music.load(f'assets/sound/music/{self.music_list[self.actual_music]}.mp3')
            pygame.mixer.music.play(loops=-1,fade_ms=1500)
            pygame.mixer.music.set_volume(0.5)
            self.music_play = True

    def pause_music(self):
        """Pausa a música.
        """
        if self.music_change:
            self.music_play = False
            self.music_pause = False
            self.music_change = False
        else:
            # Pause da música
            if self.music_pause:
                self.music_pause = False
                pygame.mixer.music.unpause()
            else:
                self.music_pause = True 
                pygame.mixer.music.pause()

    def music_select(self):
        """Seleciona a música.
        """
        if self.music_pause:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_j] and self.current_ticks - self.last_change > 150:
                self.last_change = self.current_ticks
                self.music_change = True

                pygame.mixer.music.stop()

                self.actual_music += 1

                if self.actual_music == 3:
                    self.actual_music = 0

                pygame.mixer.music.unload()
                pygame.mixer.music.load(f'assets/sound/music/{self.music_list[self.actual_music]}.mp3')
