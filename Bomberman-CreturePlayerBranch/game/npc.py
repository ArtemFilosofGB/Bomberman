import pygame

from сreature import Creature


class Npc(Creature):
    def __init__(self, x: int, y: int, image: pygame.Surface):
        super().__init__(x, y, image)


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_collision(self, other: Creature):
        return self.rect.collidepoint(other.x, other.y)

