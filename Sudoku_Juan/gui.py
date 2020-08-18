import pygame, sys, time
from pygame.locals import *
from solver import *
from tests import *

# CONSTANTS
SCREEN_SIZE = (600, 700)
MARGIN = 30
SQUARE_LENGTH = (SCREEN_SIZE[0] - (MARGIN * 2)) / 9
BLACK = (0, 0, 0)
RED = (250, 0, 0)
GREEN = (0, 250, 0)
WHITE = (250, 250, 250)
KEY_MAP = {
    K_1 : "1",
    K_2 : "2",
    K_3 : "3",
    K_4 : "4",
    K_5 : "5",
    K_6 : "6",
    K_7 : "7",
    K_8 : "8",
    K_9 : "9"
}

# INITIALIZATION
pygame.font.init()
font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
clock = pygame.time.Clock()

#OBJECTS
class Square:
    def __init__(self, col, row, val = 0):
        self.row = row
        self.col = col
        self.x = MARGIN + (col * SQUARE_LENGTH)
        self.y = MARGIN + (row * SQUARE_LENGTH)
        self.rect = pygame.Rect(self.x, self.y, SQUARE_LENGTH, SQUARE_LENGTH)
        self.val = val
        self.notes = set()
        self.selected = False

    def draw(self):
        if self.selected:
            pygame.draw.rect(screen, RED , self.rect, 3)
        if self.val != '.':
            text = font.render(self.val, 1, BLACK)
            x = self.x + ((SQUARE_LENGTH - text.get_width()) / 2)
            y = self.y + ((SQUARE_LENGTH - text.get_height()) / 2)
            screen.blit(text, (x, y))

    def get_rect(self):
        return self.rect

    def set_select(self, selected = True):
        self.selected = selected
        return self
    
    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val

    def set_note(self, note):
        self.notes.add(note)

    def remove_note(self, note):
        if note in self.notes:
            self.notes.remove(note)
            return True
        else:
            return False
    
class Board:
    def __init__(self, board):
        self.squares = [[Square(i, j, board[i][j]) for i in range(9)] for j in range(9)]
        self.problemState = ProblemState(board)
        self.selectedSquare = None
        self.notesMode = False

    def get_squares(self):
        return sum(self.squares, [])

    def get_square(self, row, col):
        return self.squares[row][col]

    def set_selected(self, square):
        if self.get_selected(): self.get_selected().set_select(False)
        self.selectedSquare = square
        square.set_select()

    def get_selected(self):
        return self.selectedSquare
    
    def add_entry(self, entry):
        if self.selectedSquare == None: return
        if self.notesMode:
            self.selectedSquare.set_note(entry)
        else:
            self.selectedSquare.set_val(entry)

    def draw(self):
        for i in range(10):
            width = 1 if i % 3 else 3
            horizontalStart = (MARGIN, MARGIN + (i * SQUARE_LENGTH))
            horizontalEnd = (SCREEN_SIZE[0] - MARGIN, MARGIN + (i * SQUARE_LENGTH))
            verticalStart = (MARGIN + (i * SQUARE_LENGTH), MARGIN)
            verticalEnd = (MARGIN + (i * SQUARE_LENGTH), SCREEN_SIZE[0] - MARGIN)

            pygame.draw.line(screen, BLACK, horizontalStart, horizontalEnd, width)
            pygame.draw.line(screen, BLACK, verticalStart, verticalEnd, width)

        for i in range(9):
            for j in range(9):
                self.squares[i][j].draw()

def main(board):

    state = Board(board)
    key = None
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for square in state.get_squares():
                    if square.get_rect().collidepoint(pos):
                        state.set_selected(square.set_select())
            if event.type == KEYDOWN:
                if event.key in KEY_MAP:
                    key = KEY_MAP[event.key]
                elif event.key == pygame.K_RIGHT:
                    moving_right = True
                elif event.key == pygame.K_LEFT:
                    moving_left = True
                elif event.key == pygame.K_UP:
                    moving_up = True
                elif event.key == pygame.K_DOWN:
                    moving_down = True
            # if event.type == KEYUP:
            #     if event.key == pygame.K_RIGHT:
            #         moving_right = False
            #     elif event.key == pygame.K_LEFT:
            #         moving_left = False
            #     elif event.key == pygame.K_UP:
            #         moving_up = False
            #     elif event.key == pygame.K_DOWN:
            #         moving_down = False
                        
        screen.fill((255, 255, 255))

        square = state.get_selected()
        if square:
            row, col = square.row, square.col
            print(row, col)
            if key:
                square.set_val(key)
                key = None
            elif moving_left and col != 0:
                state.set_selected(state.get_square(row, col - 1))
                moving_left = False
            elif moving_right and col != 8:
                state.set_selected(state.get_square(row, col + 1))
                moving_right = False
            elif moving_up and row != 0:
                state.set_selected(state.get_square(row - 1, col))
                moving_up = False
            elif moving_down and row != 8:
                state.set_selected(state.get_square(row + 1, col))
                moving_down = False

        state.draw()
        pygame.display.update()
        clock.tick(60)

tests = Tests()
main(tests.test())

pygame.quit()
sys.exit()