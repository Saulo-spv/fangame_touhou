"""Classe Background

Módulo responsável por implementar a classe Background, que representa o background do jogo.

"""
import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, screen_size: tuple[int, int], initial_pos: int, speed: int, filename: str):
        """Inicializa uma nova instância da classe Background.

        Parameters
        ----------
        screen_size : tuple[int, int]
            O tamanho da tela.
        initial_pos : int
            A posição vertical inicial da imagem.
        speed : int
            A velocidade de movimento da imagem.
        filename : str
            O nome do arquivo da imagem.
        """
        super().__init__()

        # Tamanho da tela e velocidade de movimento
        self.screen_size = screen_size
        self.initial_pos = initial_pos
        self.speed = speed

        # Carrega e configura a imagem
        self.image = pygame.Surface(self.screen_size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0,0)
        self.background = pygame.image.load(filename).convert()

        # Posição inicial da imagem
        self.y = self.initial_pos
    
    def update(self):
        """Atualiza o background.
        """
        # Atualiza a posição da imagem
        self.y += self.speed

        # Exibe a imagem
        self.image.blit(self.background, (0, self.y))

        # Reinicia a posição quando necessário
        if self.y >= 0:
            self.y = self.initial_pos + self.screen_size[1]