
import pygame

from pygame.locals import *

pygame.init()

#set up the window
screen = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('drawing')

black = (  0,   0,   0)
white = (255, 255, 255)
red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)

screen.fill(white)

pygame.draw.polygon(screen, green, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

