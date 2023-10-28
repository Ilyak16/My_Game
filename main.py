import math
import pygame
import sys

import Button
from Button import ImageButton
def Quit():
    pygame.quit()
    sys.exit()

def Play():
    pygame.init()
    window.fill((255, 255, 255))
    res = (400, 400)
    screen = pygame.transform.scale(window, res)
    pygame.transform.scale(window, res)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        window.blit(pygame.transform.scale(screen, res), (0, 0))
        clock.tick(60)
        pygame.display.update()

































pygame.init()
pygame.display.set_caption("RTS_GAME")
icon = pygame.image.load("images/icon.png")
pre_fon = pygame.image.load("images/Заставка.png")
nas = pygame.image.load("images/RTS_GAME.png")
nas.set_colorkey('White')
mest_nas = nas.get_rect(center=(620, 150))
pygame.display.set_icon(icon)
Width = 1240
Height = 900
clock = pygame.time.Clock()
window = pygame.display.set_mode((Width, Height))


window.blit(nas, mest_nas)
button_PLAY = Button.ImageButton(Width/2 - (250/2), 300, 250, 75, "PLAY", "images/Кнопка_до.png", "images/Кнопка_после.png", "Sounds/Klick.mp3")
button_QUIT = Button.ImageButton(Width/2 - (250/2), 400, 250, 75, "QUIT", "images/Кнопка_до.png", "images/Кнопка_после.png", "Sounds/Klick.mp3")
pygame.display.update()
def main_menu():
    running = True
    while running:
        window.blit(pre_fon, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == button_QUIT:
                Quit()
            if event.type == pygame.USEREVENT and event.button == button_PLAY:
                Play()
            for btn in [button_QUIT, button_PLAY]:
                btn.handle_event(event)
        for btn in [button_QUIT, button_PLAY]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.Draw(window)
        window.blit(nas, mest_nas)

        pygame.display.flip()


main_menu()

#    while run:


