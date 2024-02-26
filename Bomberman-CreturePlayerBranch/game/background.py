import pygame


class Background:
    def __init__(self, screen_width: int, screen_height: int):

        self.tile_image = pygame.image.load("../assets/Background/Blue.png").convert()
        self.tile_image = pygame.transform.scale(self.tile_image, (128, 128))

        self.horizontal_tiles_num = (screen_width // self.tile_image.get_width()) + 1
        self.vertical_tiles_num = (screen_height // self.tile_image.get_height()) + 1

    def draw(self, screen: pygame.Surface):
        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the tiled background
        for x in range(self.horizontal_tiles_num):
            for y in range(self.vertical_tiles_num):
                tile_x = x * self.tile_image.get_width()
                tile_y = y * self.tile_image.get_height()

                # Draw the tile
                screen.blit(self.tile_image, (tile_x, tile_y))
