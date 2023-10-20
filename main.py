import math
from Window import Window
import pygame
pygame.init()
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
win = Window.window(1240, 900)
win = pygame.display.set_mode((win.width, win.height))
pygame.display.set_caption("RTS_GAME")
clock = pygame.time.Clock()
while True:
    win.fill((0, 100, 0))
    for event in pygame.event.get(): # ДЛа
        if event.type == pygame.QUIT:
            exit()
    clock.tick(60)
    pygame.display.update()

