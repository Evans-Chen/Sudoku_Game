import pygame, sys
from pygame.locals import *

pygame.init()
width = 500
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sudoku')

black = (  0,   0,   0)
white = (255, 255, 255)
red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)

cellx = width/9
celly = height/10

class currentCell:
    def __init__(self):
        self.row = -1
        self.col = -1
    def update(self, row, col):
        self.row = row
        self.col = col 

currentCell = currentCell()

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

    if (currentCell.row > -1 and currentCell.col > -1):
        pygame.draw.rect(screen, red, (cellx*currentCell.col,celly*currentCell.row,cellx,celly), 4)

    if pygame.mouse.get_pressed()[0]:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        print("x: ", x)
        print("y: ", y)
        currentCell.row = y // int(celly)
        currentCell.col = x // int(cellx)
        print("currentCell.row: ", currentCell.row)
        print("currentCell.col: ", currentCell.col)
    #for event in pygame.event.get():
    #    print(event)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

