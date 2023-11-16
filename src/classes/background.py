import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, screen_size, initial_pos, speed, filename):
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
    
    def get_surface(self):
        return self.image
    
    def update(self):
        # Atualiza a posição da imagem
        self.y += self.speed

        # Exibe a imagem
        self.image.blit(self.background, (0, self.y))

        # Reinicia a posição quando necessário
        if self.y >= 0:
            self.y = self.initial_pos + self.screen_size[1]