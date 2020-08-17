import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Display

screen = py.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
while running:
    for event in py.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((255, 255, 255))
    py.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    py.display.flip()
    c
pg.quit()
sys.exit()