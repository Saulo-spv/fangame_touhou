import pygame
import sys

class Button:
    def __init__(self, x, y, width, height, text, font="carlito", font_size=20, color_text="WHITE", color_button="BLACK", color_selected="GRAY"):
        self.rect = pygame.Rect(x, y, width, height)
        self._text = text
        self.__font_name = font
        self.__font_size = font_size
        self.__font = pygame.font.Font(pygame.font.match_font(self.__font_name), font_size)
        self.__color_text = color_text
        self.__color_button_default = color_button
        self.__color_selected = color_selected
        self.__selected = False

    def draw(self, screen):
        self.update()
        pygame.draw.rect(screen, self.__color_selected if self.__selected else self.__color_button_default, self.rect)
        text_surface = self.__font.render(self._text, True, self.__color_text)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self):
        self.__selected = self.rect.collidepoint(pygame.mouse.get_pos())