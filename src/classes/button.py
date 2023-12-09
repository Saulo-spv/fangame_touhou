"""Classe Button

Módulo responsável por implementar a classe Button, que representa um botão do jogo.

"""
import pygame


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str, font: str = "carlito",
                 font_size: int =20, color_text: str ="WHITE", color_button: str ="BLACK", color_selected: str ="GRAY"):
        """Inicializa uma nova instância da classe Button.

        Parameters
        ----------
        x : int
            Posição horizontal do botão.
        y : int
            Posição vertical do botão.
        width : int
            Largura do botão.
        height : int
            Altura do botão.
        text : str
            Texto do botão.
        font : str, optional
            Fonte do texto, by default "carlito"
        font_size : int, optional
            Tamanho da fonte, by default 20
        color_text : str, optional
            Cor do texto, by default "WHITE"
        color_button : str, optional
            Cor do botão, by default "BLACK"
        color_selected : str, optional
            Cor do botão ao ser selecionado, by default "GRAY"
        """
        self.rect = pygame.Rect(x, y, width, height)

        self.__text = text
        self.__font_name = font
        self.__font_size = font_size
        self.__font = pygame.font.Font(pygame.font.match_font(self.__font_name), self.__font_size)

        self.__color_text = color_text
        self.__color_button_default = color_button
        self.__color_selected = color_selected

        self.__selected = False

    def draw(self, screen):
        """Desenha o botão na tela.

        Parameters
        ----------
        screen : pygame.Surface
            A tela do jogo.
        """
        self.update()

        pygame.draw.rect(screen, self.__color_selected if self.__selected else self.__color_button_default, self.rect)

        text_surface = self.__font.render(self.__text, True, self.__color_text)
        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)

    def update(self):
        """Atualiza o botão.
        """
        self.__selected = self.rect.collidepoint(pygame.mouse.get_pos())