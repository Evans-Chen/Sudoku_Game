from collections import deque

class Positions:
    def __init__(self):
        self.row = set()
        self.col = set()
        self.grid = set()
        
    def addStep(self, step):
        i, j = step
        grid = (i // 3) * 3 + (j // 3)
        self.row.add(i)
        self.col.add(j)
        self.grid.add(grid)
        
    def removeStep(self, step):
        i, j = step
        grid = (i // 3) * 3 + (j // 3)
        self.row.remove(i)
        self.col.remove(j)
        self.grid.remove(grid)       
        
    def validStep(self, step):
        i, j = step
        grid = (i // 3) * 3 + (j // 3)
        if i in self.row: return False
        if j in self.col: return False
        if grid in self.grid: return False
        return True
    
class ProblemState:   
    def __init__(self, board):
        self.board = board
        self.empty, self.positions = self.createProblemState()

    def getBoard(self):
        return self.board
    
    def updateBoard(self, move, step, remove = False):
        i, j = step
        self.board[i][j] = '.' if remove else move
            
    def createProblemState(self):
        empty = deque()
        positions = [Positions() for i in range(9)]
            
        for i in range(9):
            for j in range(9):
                val = self.board[i][j]
                step = (i, j)
                if val == '.': empty.append(step)
                else: positions[int(val) - 1].addStep(step)
        return empty, positions
    
    def isComplete(self):
        return not self.empty

    def getNextStep(self):
        return self.empty[0]
    
    def getPossibleMoves(self, step):
        P = self.positions
        return [position for position in range(9) if P[position].validStep(step)]

    def makeMove(self, step, move):
        self.positions[move].addStep(step)
        self.updateBoard(str(move + 1), step)
        self.empty.popleft()
        return self

    def undoMove(self, step, move):
        self.positions[move].removeStep(step)
        self.updateBoard(str(move + 1), step, True)
        self.empty.appendleft(step)
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
        board = state.getBoard()
        return None
        