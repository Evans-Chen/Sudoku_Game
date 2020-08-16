import pygame as py
from pygame.locals import (
    K_0,
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_6,
    K_7,
    K_8,
    K_9,
    K_n,
    MOUSEMOTION,
    QUIT,
)
# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# initialize objects
py.init()
screen = py.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    screen.fill((255, 255, 255))
    py.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    py.display.flip()
py.quit()