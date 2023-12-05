import pygame

class Button:
    def __init__(self, x, y, width, height, text, font="carlito", font_size=20, color_text="WHITE", color_button="BLACK"):
        self.rect = pygame.Rect(x, y, width, height)
        self._text = text
        self.__font_name = font 
        self.__font_size = font_size
        self.__font = pygame.font.Font(pygame.font.match_font(self.font_name), font_size)
        self.__color = color_text
        self.__color_button = color_button

    def draw(self, screen):
        pygame.draw.rect(screen, self.color_button, self.rect)
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
