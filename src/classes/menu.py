import pygame
import sys
from classes.button import Button

class Menu:
    def __init__(self):

        # Tela Inicial do Menu
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 800, 600
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Menu")

        # Carrega e Redimensiona o Background
        original_bg = pygame.image.load("assets/images/background/menu_inicial.png")
        self.BG = pygame.transform.scale(original_bg, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.play_button = Button(x=105, y=200, width=150, height=50, text="PLAY")
        self.options_button = Button(x=80, y=300, width=220, height=50, text="OPTIONS")
        self.quit_button = Button(x=105, y=400, width=150, height=50, text="QUIT")

        # define quando o jogo começa
        self.start_game = False

    def play(self):
        self.start_game = True

    def options(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill("white")

            # Cria Botão Para Voltar
            OPTIONS_BACK = Button(x=400, y=450, width=200, height=50, text="BACK")
            OPTIONS_BACK.update()
            OPTIONS_BACK.draw(self.SCREEN)

            # Verifica Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.rect.collidepoint(OPTIONS_MOUSE_POS):
                        return

            pygame.display.update()

    # Verifica eventos
    def update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.rect.collidepoint(event.pos):
                    self.play()
                elif self.options_button.rect.collidepoint(event.pos):
                    self.options()
                elif self.quit_button.rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

    def main_menu(self):
        while not self.start_game:
            self.SCREEN.blit(self.BG, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_TEXT = pygame.font.Font(None, 100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))
            self.SCREEN.blit(MENU_TEXT, MENU_RECT)


            # Desenha e Atualiza os botões
            self.play_button.draw(self.SCREEN)
            self.options_button.draw(self.SCREEN)
            self.quit_button.draw(self.SCREEN)

            self.update_events()

            pygame.display.update()

            
    def run_menu(self):
        self.main_menu()