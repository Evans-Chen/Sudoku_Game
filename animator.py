import pygame 
from pygame.locals import *
import sys 

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

#Initialize the font
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

#Initialize some colors
black = (  0,   0,   0)
white = (255, 255, 255)
red   = (255,   0,   0)
green = (  0, 255,   0)

cellx = width/9
celly = height/10

originalNumbers = {}

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

for row in range(len(board)):
    for col in range(len(board[0])):
        if board[row][col] != ".":
            originalNumbers[(row, col)] = board[row][col]

##################################################
##########   Main Game Loop   ####################
##################################################

while True:
    #clock.tick(FPS)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for col in range(10):
        top = [int(cellx*col), 0]
        bottom = [int(cellx*col), int(height-celly)]
        if col%3 == 0:
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
        if row%3 == 0:
            thickness = 5
        else:
            thickness = 1
        pygame.draw.lines(screen, black, True, [left, right], thickness)

    #Displays the original numbers
    for cell in originalNumbers:
        number = myfont.render(originalNumbers[cell], True, black)
        location = number.get_rect()
        location.center = (int(cell[1]*cellx+cellx/2), int(cell[0]*celly+celly/2))
        screen.blit(number, location)

    

    pygame.display.update()

class Positions:
    def __init__(self):
        self.row = set()
        self.col = set()
        self.grid = set()
    def add(self, row, col):
        self.row.add(row)
        self.col.add(col)
        self.grid.add((row//3)*3+(col//3))
    def delete(self, row, col):
        self.row.remove(row)
        self.col.remove(col)
        self.grid.remove((row//3)*3+(col//3))

class Solution:
    def solveSudoku(self, board):
        self.positions = [None]*10
        self.emptyCells = []

        for i in range(1, 10):
            self.positions[i] = Positions()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    self.positions[int(board[row][col])].add(row, col)
                else:
                    self.emptyCells.append((row, col))

        board = self.solveWithBacktracking(board)

    def solveWithBacktracking(self, board):
        if self.isComplete():
            return board
        nextStep = self.emptyCells[0]
        for move in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.isValid(board, nextStep, int(move)):
                board = self.makeMove(board, nextStep, move)
                tmpSolution = self.solveWithBacktracking(board)
                if tmpSolution != None:
                    return tmpSolution
                board = self.undoMove(board, nextStep, move)

        return None

    def isComplete(self):
        return len(self.emptyCells) == 0

    def getNextStep(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    return (row, col)

    def isValid(self, board, nextStep, move):
        if nextStep[0] in self.positions[move].row: return False
        if nextStep[1] in self.positions[move].col: return False
        if (nextStep[0]//3)*3+(nextStep[1]//3) in self.positions[move].grid: return False
        return True

    def makeMove(self, board, nextStep, move):
        board[nextStep[0]][nextStep[1]] = move
        self.positions[int(move)].add(nextStep[0], nextStep[1])
        self.emptyCells.pop(0)
        return board

    def undoMove(self, board, nextStep, move):
        board[nextStep[0]][nextStep[1]] = "."
        self.positions[int(move)].delete(nextStep[0], nextStep[1])
        self.emptyCells.insert(0, nextStep)
        return board

