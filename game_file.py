import pygame, sys, time
from pygame.locals import *

##################################################
##########   Initialization   ####################
##################################################

#Initialize pygame
pygame.init()
width = 500
height = 600
#Create the window where the game will be displayed
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sudoku')
#clock = pygame.time.Clock()

#Initialize the font
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

#Initialize some colors
black = (  0,   0,   0)
white = (255, 255, 255)
red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)
grey  = (128, 128, 128)

cellx = width/9
celly = height/10

numbers = set([pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9])

originalNumbers = {}
userNumbers = {}

class currentCell:
    def __init__(self):
        self.row = -1
        self.col = -1
        self.active = False

currentCell = currentCell()

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

for row in range(len(board)):
    for col in range(len(board[0])):
        if (board[row][col] != "."):
            originalNumbers[(row,col)] = board[row][col]

##################################################
##########   Main Game Loop   ####################
##################################################

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    for col in range(10):
        top = [int(cellx*col),0]
        bottom = [int(cellx*col),int(height-celly)]
        if col%3==0:
            thickness = 5
        else:
            thickness = 1
        if col == 9:
            top[0] -= 1
            bottom[0] -= 1
        pygame.draw.lines(screen, black, True, [top, bottom], thickness)

    for row in range(10):
        left = [0, int(celly*row)]
        right = [width, int(celly*row)]
        if row%3==0:
            thickness = 5
        else:
            thickness = 1
        pygame.draw.lines(screen, black, True, [left, right], thickness)

    if (currentCell.active):
        pygame.draw.rect(screen, red, (int(cellx*currentCell.col),int(celly*currentCell.row),int(cellx),int(celly)), 5)

    #pygame.mouse.get_pressed() -> (button1, button2, button3) these are all bools
    if pygame.mouse.get_pressed()[0]:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        #print("x: ", x)
        #print("y: ", y)
        currentCell.row = y // int(celly)
        currentCell.col = x // int(cellx)
        currentCell.active = True
        #print("currentCell.row: ", currentCell.row)
        #print("currentCell.col: ", currentCell.col)
    
    '''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key in numbers and currentCell.active:
                userNumbers[(currentCell.row,currentCell.col)] = event.key
    '''

    keys = pygame.key.get_pressed()
    if (currentCell.row, currentCell.col) not in originalNumbers:
        if keys[pygame.K_0]:
            userNumbers[(currentCell.row, currentCell.col)] = "0"
        if keys[pygame.K_1]:
            userNumbers[(currentCell.row, currentCell.col)] = "1"
        if keys[pygame.K_2]:
            userNumbers[(currentCell.row, currentCell.col)] = "2"
        if keys[pygame.K_3]:
            userNumbers[(currentCell.row, currentCell.col)] = "3"
        if keys[pygame.K_4]:
            userNumbers[(currentCell.row, currentCell.col)] = "4"
        if keys[pygame.K_5]:
            userNumbers[(currentCell.row, currentCell.col)] = "5"
        if keys[pygame.K_6]:
            userNumbers[(currentCell.row, currentCell.col)] = "6"
        if keys[pygame.K_7]:
            userNumbers[(currentCell.row, currentCell.col)] = "7"
        if keys[pygame.K_8]:
            userNumbers[(currentCell.row, currentCell.col)] = "8"
        if keys[pygame.K_9]:
            userNumbers[(currentCell.row, currentCell.col)] = "9"

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and currentCell.row > 0:
                print("up")
                currentCell.row -= 1
            if event.key == pygame.K_DOWN and currentCell.row < 8:
                print("down")
                currentCell.row += 1
            if event.key == pygame.K_LEFT and currentCell.col > 0:
                print("left")
                currentCell.col -= 1
            if event.key == pygame.K_RIGHT and currentCell.col < 8:
                print("right")
                currentCell.col += 1

    #Display the user's numbers
    for cell in userNumbers:
        number = myfont.render(userNumbers[cell],True,grey)
        location = number.get_rect()
        location.center = (int(cell[1]*cellx+cellx/2), int(cell[0]*celly+celly/2))
        #print("cell: ", cell)
        #print("x: ", int(cell[1]*col))
        #print("y: ", int(cell[0]*row))
        screen.blit(number, location) 
    
    #Displays the original numbers
    for cell in originalNumbers:
        number = myfont.render(originalNumbers[cell],True,black)
        location = number.get_rect()
        location.center = (int(cell[1]*cellx+cellx/2), int(cell[0]*celly+celly/2))
        screen.blit(number, location) 

    #for event in pygame.event.get():
    #    print(event)

    pygame.display.update()
    #clock.tick(60)


