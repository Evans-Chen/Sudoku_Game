import pygame, sys
from pygame.locals import *

pygame.init()

black = (  0,   0,   0)
white = (255, 255, 255)
red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)

width = 900
height = 1000

cellx = width/9
celly = height/10

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sudoku')

running = True
while running:

    screen.fill(white)
    
    for col in range(10):
        top = [cellx*col,0]
        bottom = [cellx*col,height-celly]
        if (col%3==0):
            thickness = 3
        else:
            thickness = 1
        if col == 9:
            top[0] -= 1
            bottom[0] -= 1
        pygame.draw.lines(screen, black, True, [top, bottom], thickness)

    for row in range(10):
        left = [0, celly*row]
        right = [width, celly*row]
        if (row%3==0):
            thickness = 3
        else:
            thickness = 1
        pygame.draw.lines(screen, black, True, [left, right], thickness)



    pygame.display.update()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

