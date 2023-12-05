import pygame
import sys
import subprocess
from classes.button import Button

pygame.init()

# Tela Inicial do Menu
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

# Carrega e Redimensiona o Background
original_bg = pygame.image.load("assets/images/background/menu_inicial.png")
BG = pygame.transform.scale(original_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Logica Botão Play
def play():
    pygame.quit()
    subprocess.run([sys.executable, "src/main.py"])
    sys.exit()

# Logica Botão Options
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        # Cria Botão Para Voltar
        OPTIONS_BACK = Button(x=400, y=450, width=200, height=50, text="BACK", color_button="Black")
        OPTIONS_BACK.update()
        OPTIONS_BACK.draw(SCREEN)

        # Verifica Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.rect.collidepoint(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Escreve MAIN MENU
        MENU_TEXT = pygame.font.Font(None, 100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Cria os Botões
        PLAY_BUTTON = Button(x=105, y=200, width=150, height=50, text="PLAY")
        OPTIONS_BUTTON = Button(x=80, y=300, width=220, height=50, text="OPTIONS")
        QUIT_BUTTON = Button(x=105, y=400, width=150, height=50, text="QUIT")
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.update()
            button.draw(SCREEN)

        # Verifica Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.rect.collidepoint(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.rect.collidepoint(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.rect.collidepoint(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()