import pygame
from settings import tile_size
from tile import Tile


class Level:

    def __init__(self, level_layout: list, surface):
        self.tiles = pygame.sprite.Group()
        self.display_surface = surface
        self.world_shift = 0
        self.generate_level(level_layout)

    def generate_level(self, layout: list):
        """Add instances of Tile class to the group."""
        for row_index, row in enumerate(layout):
            for column_index, cell_value in enumerate(row):
                if cell_value == 'X':
                    x = column_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)

    def run(self):
        """Scroll map by x position and draw tiles."""
        self.tiles.update(self.world_shift)  # Calls tile.update() method for every tile in the group self.tiles.
        self.tiles.draw(self.display_surface)