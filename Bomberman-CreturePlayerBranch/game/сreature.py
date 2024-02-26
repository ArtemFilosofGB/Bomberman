import pygame


class Creature:
    def __init__(self, x: int, y: int, image: pygame.Surface):
        self.x = x
        self.y = y
        self.speed = 5
        self.image = image
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (255, 0, 0), self.rect, 1)
        self.rect.x = self.x
        self.rect.y = self.y
        self.life = 3
        self.spawn_x = x
        self.spawn_y = y


    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

    def damage(self, damage: int):
        self.life -= damage
