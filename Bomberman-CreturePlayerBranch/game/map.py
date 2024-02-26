import pygame
from random import randint
from tile import Tile, TileType


class Map:
    def __init__(self, screen: pygame.Surface):
        self.grass_image = pygame.image.load("../assets/Map/grass.png").convert()
        self.border_image = pygame.image.load("../assets/Map/border_final.png").convert()
        self.destructible_image = pygame.image.load("../assets/Map/destructible.png").convert()

        self.grass_image = pygame.transform.scale(self.grass_image, (48, 48))
        self.border_image = pygame.transform.scale(self.border_image, (48, 48))
        self.destructible_image = pygame.transform.scale(self.destructible_image, (48, 48))

        self.map_width = 21
        self.map_height = 15

        self.tiles_map = [[] for _ in range(self.map_width)]

        # Calculate horizontal and vertical offsets to center the map
        self.tile_size = self.grass_image.get_width()
        map_width_pixels = self.map_width * self.tile_size
        map_height_pixels = self.map_height * self.tile_size

        self.horizontal_offset = (screen.get_width() - map_width_pixels) // 2
        self.vertical_offset = (screen.get_height() - map_height_pixels) // 2

    def create_map(self):
        for x in range(self.map_width):
            for y in range(self.map_height):
                x_pos = x * self.tile_size + self.horizontal_offset
                y_pos = y * self.tile_size + self.vertical_offset

                if (x == 0
                        or x == self.map_width - 1
                        or y == 0
                        or y == self.map_height - 1
                        or (not x % 2 and not y % 2)):
                    self.tiles_map[x].append(Tile(x_pos, y_pos, TileType.BORDER, self.border_image))
                else:
                    if (y == 1 and x == 1
                            or y == 1 and x == 2
                            or y == 2 and x == 1):
                        self.tiles_map[x].append(Tile(x_pos, y_pos, TileType.GRASS, self.grass_image))
                    elif (y == self.map_height - 2 and x == self.map_width - 3
                          or y == self.map_height - 2 and x == self.map_width - 2
                          or y == self.map_height - 3 and x == self.map_width - 2):
                        self.tiles_map[x].append(Tile(x_pos, y_pos, TileType.GRASS, self.grass_image))
                    else:
                        if randint(0, 1):
                            self.tiles_map[x].append(Tile(x_pos, y_pos, TileType.GRASS, self.grass_image))
                        else:
                            self.tiles_map[x].append(Tile(x_pos, y_pos, TileType.DESTRUCTIBLE, self.destructible_image))

    def draw(self, screen: pygame.Surface):
        for line in self.tiles_map:
            for tile in line:
                tile.draw(screen)

