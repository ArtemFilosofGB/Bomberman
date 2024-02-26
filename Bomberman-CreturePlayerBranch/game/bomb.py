import pygame
from explosions import Explosions
from pygame.sprite import Sprite

from сreature import Creature


class Bomb(Creature, pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, image: pygame.Surface):
        pygame.sprite.Sprite.__init__(self)# todo kill self
        super().__init__(x, y, image)
        self.timer = 3;  # 3 seconds todo: add timer
        self.drop_time=pygame.time.get_ticks()
        self.power = 3


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def blow_up(self):
        #todo: add sound of explosion
        #todo: add animation
        explosion = Explosions(self.x, self.y, pygame.image.load("../assets/explosion/explosion64.png"))
        explosion.pover_exp = self.power
        self.kill()
        pass
