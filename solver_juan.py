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
        if i not in onBoard:
            raise Invalid
        onBoard.remove(i)
        missing.add(i)
        
        # check that section is full
        section[2] = missing == set()
    
    def removeStep(self, step):
        i, j = step
        self.remove(self.row, i)
        self.remove(self.col, j)
        self.remove(self.grid, (i // 3) * 3 + (j // 3))
        
    def validStep(self, step):
        i, j = step
        return i in self.row[1] and j in self.col[1]
    
    def isFull(self):
        return self.row[2] and self.col[2] and self.grid[2]
    
    def __str__(self):
        s = (str(self.row), str(self.col), str(self.grid))
        return f"rows: %s\ncolumns: %s\nboxes: %s" % s
    
class ProblemState:   
    def __init__(self, board):
        self.board = board
        try:
            self.empty, self.positions = self.createProblemState()
        except Invalid:
            print("This board is invalid")

    def createProblemState(self):
        empty = deque()
        positions = defaultdict(Positions)
        for i in range(9):
            for j in range(9):
                val = self.board[i][j]
                if val == '.':
                    empty.append((i, j))
                else:
                    positions[val].append(i, j)
        return empty, positions
    
    def isComplete(self):
        return not self.empty

    def getNextStep(self):
        return self.empty.popleft()
    
    def getPossibleMoves(self, step):
        P = self.positions
        return [position for position in range(9) if P[position].validStep(step)]

    def makeMove(self, step, move):
        pos = self.positions[move]
        pos.addStep(step)
        return self

    def undoMove(self, step, move):
        pos = self.positions[move]
        pos.removeStep(step)
        return self

class Solution:
    def solveSudoku(self, board) -> None:
        state = ProblemState(board)
        def solveWithBacktracking(problemState):
            if problemState.isComplete():
                return problemState
            nextStep = problemState.getNextStep()
            for move in problemState.getPossibleMoves(nextStep):
                problemState = problemState.makeMove(nextStep, move)
                tmpSolution = solveWithBacktracking(problemState)
                if tmpSolution != None:
                    return tmpSolution
                problemState = problemState.undoMove(nextStep, move)
            return None
        state = solveWithBacktracking(state)
        return None
        