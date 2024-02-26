import pygame
from enum import Enum


class TileType(Enum):
    BORDER = 0
    GRASS = 1
    DESTRUCTIBLE = 2


class Tile:
    def __init__(self, x: int, y: int, tile_type: TileType, image: pygame.Surface):
        self.x = x
        self.y = y
        self.type = tile_type

        self.image = image

        self.hitbox = pygame.Rect(x, y, image.get_width(), image.get_height())
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))
