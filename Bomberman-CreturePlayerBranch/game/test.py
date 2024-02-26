import сreature

import pygame as py
import pygame

pygame.init()

screen = pygame.display.set_mode((1024, 800))
pygame.display.set_caption("Pygame game game")


pygame.display.set_icon(pygame.image.load("icon.bmp"))

gamerun = True
clock = pygame.time.Clock()
FPS = 60
RGB = (255, 255, 255)


while gamerun == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # закрытие игры крестиком
            pygame.quit()
            gamerun = False

    py.draw.polygon(screen, (100,100,100), [(100, 200), (200, 300), (500, 500),(800,800)])
    py.display.update()


    # pygame.time.delay(20) # задержка на 20 миллисекунд
    clock.tick(FPS)  # 60 кадров в секунду