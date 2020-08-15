from collections import defaultdict, deque

fullSet = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

class Invalid(Exception):
    pass

class Positions:
    def __init__(self):   
        self.row = [set(), set(), False]
        self.col = [set(), set(), False]
        self.grid = [set(), set(), False]
    
    def add(self, section, i):
        onBoard = section[0]
        missing = section[1]
        if i in onBoard:
            raise Invalid
        onBoard.add(i)
        missing.remove(i)
        
        # check that section is full
        section[2] = missing == set()
    
    def addStep(self, step):
        i, j = step
        self.add(self.row, i)
        self.add(self.col, j)
        self.add(self.grid, (i // 3) * 3 + (j // 3))
        
    def remove(self, section, i):
        onBoard = section[0]
        missing = section[1]
        if i in onBoard:
            raise Invalid
        onBoard.remove(i)
        missing.add(i)
        
        # check that section is full
        section[2] = missing == set()
    
    def removeStep(self, step)
        i, j = step
        self.remove(self.row, i)
        self.remove(self.col, j)
        self.remove(self.grid, (i // 3) * 3 + (j // 3))
        
    def isFull(self):
        return self.row[2] and self.col[2] and self.grid[2]
    
    def __str__(self):
        s = (str(self.row), str(self.col), str(self.grid))
        return f"rows: %s\ncolumns: %s\nboxes: %s" % s
    
class ProblemState:   
    def __init__(self, board: List[List[str]]):
        self.board = board
        try:
            self.empty, self.positions = createProblemState()
        except invalid:
            print("This board is invalid")

    def createProblemState():
        empty = deque()
        positions = defaultdict(Positions)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    empty.append((i, j))
                else:
                    positions[val].append(i, j)
        return empty, positions
    
    def isComplete
    
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        problemState = ProblemState(board)
        if isComplete(problemState):
            return None
        nextStep = getNextStep(problemState)
        for move in getPossibleMoves(problemState, nextStep):
            # Sometimes it's easier to make a move, then check if it's valid.
            # Sometimes it's easier to check if a move is valid first.
            # Just make sure that you always undo a move properly!
            if isValid(problemState, nextStep, move):
                problemState = makeMove(problemState, nextStep, move)
                tmpSolution = solveWithBacktracking(problemState)
                if tmpSolution != None:
                    return tmpSolution
                problemState = undoMove(problemState, nextStep, move)
        return None
        