"""Classe Effect

Classe responsável por implementar os efeitos visuais do jogo.

"""
import pygame

class Effect(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], type: str):
        """Inicializa uma nova instância da classe Effect.

        Parameters
        ----------
        pos : tuple[int, int]
            A posição inicial do efeito.
        type : str
            O tipo do efeito.
        """
        super().__init__()

        self.type = type

        # Configura as imagens do efeito
        if self.type == 'explosion_1':
            self.__images = [pygame.image.load(f'assets/images/effects/explosion_1_{i}.png').convert_alpha() for i in range(4)]
            self.__images = [pygame.transform.scale(image, (30, 30)) for image in self.__images]
        elif self.type == 'explosion_2':
            self.__images = [pygame.image.load(f'assets/images/effects/explosion_2_{i}.png').convert_alpha() for i in range(3)]
            self.__images = [pygame.transform.scale(image, (40, 40)) for image in self.__images]

        # Configura a imagem inicial do efeito
        self.__index = 0
        self.image = self.__images[self.__index]

        # Posição do efeito
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # Configurações de animação
        self.__last_frame_time = 0
        self.__animation_cooldown = 100
    
    def update(self):
        """Atualiza o efeito.
        """
        current_time = pygame.time.get_ticks()

        # Atualiza a animação
        if current_time - self.__last_frame_time > self.__animation_cooldown:
            self.__last_frame_time = pygame.time.get_ticks()

            self.__index += 1

            # Verifica se o efeito acabou
            if self.__index >= len(self.__images):
                self.kill()
            else:
                self.image = self.__images[self.__index]
            