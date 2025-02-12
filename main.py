import pygame
from settings import *
from map import *

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

RUN = True

map = Map()

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.fill((0,0,0))

    map.render(screen)

    pygame.display.update()