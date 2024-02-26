import pygame as py

from player import Player


def readKeyboard(player: Player, player_controls: int):
    #print(player.rect.x, player.rect.y)

        # Проверка когда клавиша нажимается
    keys = py.key.get_pressed() # возвращает словарь с нажатыми клавишами и их состояниями, нет Shift Ctrl Alt
    if keys[py.K_ESCAPE]:
        py.quit()
        quit()
# For pale
    if player_controls == 1:
        if keys[py.K_LEFT]:
            player.rect.x -= player.speed
        if keys[py.K_RIGHT]:
            player.rect.x += player.speed
        if keys[py.K_UP]:
            player.rect.y -= player.speed
        if keys[py.K_DOWN]:
            player.rect.y += player.speed
        if keys[py.K_o]:
            player.drop_bomb()
        if keys[py.K_p]:
            player.action()

    if player_controls ==2:
        if keys[py.K_a]:
            player.rect.x -= player.speed
        if keys[py.K_d]:
            player.rect.x += player.speed
        if keys[py.K_w]:
            player.rect.y -= player.speed
        if keys[py.K_s]:
            player.rect.y += player.speed
        if keys[py.K_f]:
            player.drop_bomb()
        if keys[py.K_g]:
            player.action()



