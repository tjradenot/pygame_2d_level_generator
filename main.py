import pygame
import sys
from settings import *
from level import Level


def move_level_map(event):
    print('Use LEFT and RIGHT arrow keys to change movement and SPACE to stop moving.')
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        level.world_shift = -2
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        level.world_shift = 2
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        level.world_shift = 0


pygame.init()
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        move_level_map(event)

    screen.fill((80, 80, 80))
    level.run()
    pygame.display.update()
    clock.tick(60)
