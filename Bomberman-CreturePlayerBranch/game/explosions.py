import pygame

from сreature import Creature


class Explosions(Creature):
    def __init__(self, x: int, y: int, image: pygame.Surface):
        super().__init__(x, y, image)
        self.pover_exp = 1
        self.timer_exp = 0

    def draw_exp(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))


