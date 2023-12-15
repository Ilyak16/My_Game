import math
import pygame
import sys
import time
import random
import Button

from Button import ImageButton
def Quit():
    pygame.quit()
    sys.exit()

class Player:
    def __init__(self, x, y, width, height, model, HP, speed):
        self.player_x = x
        self.player_y = y
        self.width_player = width
        self.height_player = height
        self.model = pygame.transform.scale(pygame.image.load(model), (width, height))
        self.HP = HP
        self.speed = speed
class Enemy:
    def __init__(self, x, y, width, height, model, HP, speed):
        self.enemy_x = x
        self.enemy_y = y
        self.width = width
        self.height = height
        self.model = pygame.transform.scale(pygame.image.load(model), (width, height))
        self.HP = HP
        self.speed = speed
pygame.init()
# Создание иконки, заднего фона, названия и его обработка
pygame.display.set_caption("GAME")
icon = pygame.image.load("images/icon.png")
pre_fon = pygame.image.load("images/Заставка.png")
nas = pygame.image.load("images/COSMO.png")
mest_nas = nas.get_rect(center=(620, 150))
nas.set_colorkey('Black')
my_font = pygame.font.Font("Fonts/bionicle-training-card-font-2-4.ttf", 20)
Score = my_font.render("SCORE ", False, (255, 255, 255))
# Создание игрока с помощью класса
gamer = Player(495, 660, 250, 240, "images/Player.png", 3, 10)
#  Создание пули и списка под них
bullet = pygame.transform.scale(pygame.image.load("images/Shot2.png"), (70, 70))
bullets = []
# Создание врагов с помощью класса и списка под них
enemy = Enemy(0, 0, 150, 167, "images/Enemy.png", 1, 5)
enemies = []
# Установка иконки, ширины и высоты экрана, ограничение фпс, названия
pygame.display.set_icon(icon)
Width = 1240
Height = 900
HS_z = int(0)
clock = pygame.time.Clock()
window = pygame.display.set_mode((Width, Height))
window.blit(nas, mest_nas)
# Создание кнопок с помощью класса
button_PLAY = Button.ImageButton(Width/2 - (250/2), 300, 250, 75, "PLAY", "images/Кнопка_до.png", "images/Кнопка_после.png")#, "Sounds/Klick.mp3"
button_QUIT = Button.ImageButton(Width/2 - (250/2), 500, 250, 75, "QUIT", "images/Кнопка_до.png", "images/Кнопка_после.png")#, "Sounds/Klick.mp3"
button_OPTION = Button.ImageButton(Width/2 - (250/2), 400, 250, 75, "OPTION", "images/Кнопка_до.png", "images/Кнопка_после.png")
# Создаём функцию игры
def Play():
    # Создание фона, таймера и ограничителя фпс и задавание здоровья игрока
    clock = pygame.time.Clock()
    Fon = pygame.image.load("images/Fon.jpg")
    Fon = pygame.transform.scale(Fon, (1240, 900))
    spawn_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_timer, 1000)
    gamer.HP = 3
    Score_z = 0
    per = 0
    gaming = True
    while gaming:
        # Вывод фона, отрисовка игрока, нахождение рандом места спавна, наделение игрока моделькой
        window.blit(Fon, (0, 0))
        window.blit(Score, (0, 0))
        window.blit(my_font.render(str(Score_z), False, (255, 255, 255)), (70, 0))
        window.blit(gamer.model, (gamer.player_x, gamer.player_y))
        enemy.enemy_x = random.randint(0, 1090)
        gamer_rect = gamer.model.get_rect(topleft=(gamer.player_x, gamer.player_y))
        # перебор врагов в списке
        for (e, el) in enumerate(enemies):
            window.blit(enemy.model, (el.x, el.y))
            el.y += enemy.speed
            if gamer_rect.colliderect(el):
                gamer.HP = 0
            if el.y > Height:
                enemies.pop(e)
        # Перебор пуль в списке
        if bullets:
            for (i, el) in enumerate(bullets):
                window.blit(bullet, (el.x, el.y))
                el.y -= 10
                if el.y < -70:
                    bullets.pop(i)
                if enemies:
                    for (ind, elm) in enumerate(enemies):
                        if el.colliderect(elm):
                            enemies.pop(ind)
                            bullets.pop(i)
                            Score_z += 125
        # Проверка на действия игрока
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and gamer.player_x > 0:
            per = -gamer.speed
            gamer.player_x += per
        elif keys[pygame.K_d] and gamer.player_x < Width - gamer.width_player:
            per = gamer.speed
            gamer.player_x += per
        else:
            per = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if gaming and event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                bullets.append(bullet.get_rect(topleft=(gamer.player_x + 90, gamer.player_y - 30)))
            if event.type == spawn_timer:
                enemies.append(enemy.model.get_rect(topleft=(enemy.enemy_x, enemy.enemy_y)))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
                for i in range(10):
                    gamer.player_x += per
                    window.blit(gamer.model, (gamer.player_x, gamer.player_y))
                    pygame.time.delay(1)
        # Проверка условий проигрыша
        if gamer.HP == 0:
            enemies.clear()
            bullets.clear()
            gaming = False
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

def main_menu():
    running = True
    while running:
        # Обновление экрана
        window.blit(pre_fon, (0, 0))
        window.blit(nas, mest_nas)
        # Проверка на действия игрока
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.USEREVENT and event.button == button_QUIT:
                Quit()
            if event.type == pygame.USEREVENT and event.button == button_PLAY:
                 Play()
            if event.type == pygame.USEREVENT and event.button == button_OPTION:
                print("455")
            for btn in [button_QUIT, button_PLAY, button_OPTION]:
                btn.click(event)
        # Проверка наведённости
        for btn in [button_QUIT, button_PLAY, button_OPTION]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.Draw(window)
        pygame.display.flip()
main_menu()




#    while run:


