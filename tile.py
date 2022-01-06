import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_position: tuple, tile_size: int):
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((255, 217, 189))
        self.rect = self.image.get_rect(topleft=tile_position)

    def update(self, x_shift):
        self.rect.x += x_shift
