import math
import pygame
import sys

import Button

from Button import ImageButton
def Quit():
    pygame.quit()
    sys.exit()

class Player:
    def __init__(self, x, y, width, height, model, HP):
        self.player_x = x
        self.player_y = y
        self.width_player = width
        self.height_player = height
        self.model = pygame.transform.scale(pygame.image.load(model), (width, height))
        self.HP = HP

pygame.init()
pygame.display.set_caption("GAME")
icon = pygame.image.load("images/icon.png")
pre_fon = pygame.image.load("images/Заставка.png")
nas = pygame.image.load("images/COSMO.png")
nas.set_colorkey('Black')
Player = Player(940, 0, 300, 150, "images/Player.png", 3)
mest_nas = nas.get_rect(center=(620, 150))
pygame.display.set_icon(icon)
Width = 1240
Height = 900
clock = pygame.time.Clock()
window = pygame.display.set_mode((Width, Height))
window.blit(nas, mest_nas)
button_PLAY = Button.ImageButton(Width/2 - (250/2), 300, 250, 75, "PLAY", "images/Кнопка_до.png", "images/Кнопка_после.png")#, "Sounds/Klick.mp3"
button_QUIT = Button.ImageButton(Width/2 - (250/2), 400, 250, 75, "QUIT", "images/Кнопка_до.png", "images/Кнопка_после.png")#, "Sounds/Klick.mp3"
pygame.display.update()
def Play():
    clock = pygame.time.Clock()
    Fon = pygame.image.load("images/Fon.png")
    window.blit(Fon, (0, 0))



    while True:



        clock.tick(60)



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
                btn.click(event)
        for btn in [button_QUIT, button_PLAY]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.Draw(window)
        window.blit(nas, mest_nas)

        pygame.display.flip()


main_menu()

#    while run:


