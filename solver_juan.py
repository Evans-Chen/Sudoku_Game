from collections import defaultdict, deque

fullSet = {0, 1, 2, 3, 4, 5, 6, 7, 8}

class Invalid(Exception):
    pass

class Positions:
    def __init__(self):
        self.row = [set(), fullSet.copy()]
        self.col = [set(), fullSet.copy()]
        self.grid = [set(), fullSet.copy()]
    
    def add(self, section, i):
        onBoard = section[0]
        missing = section[1]
        if i in onBoard: raise Invalid
        onBoard.add(i)
        missing.remove(i)
    
    def addStep(self, step):
        i, j = step
        self.add(self.row, i)
        self.add(self.col, j)
        self.add(self.grid, (i // 3) * 3 + (j // 3))
        
    def remove(self, section, i):
        onBoard = section[0]
        missing = section[1]
        if i not in onBoard: raise Invalid
        onBoard.remove(i)
        missing.add(i)
    
    def removeStep(self, step):
        i, j = step
        self.remove(self.row, i)
        self.remove(self.col, j)
        self.remove(self.grid, (i // 3) * 3 + (j // 3))
        
    def validStep(self, step):
        i, j = step
        grid = (i // 3) * 3 + (j // 3)
        return i in self.row[1] and j in self.col[1] and grid in self.grid[1]
    
class ProblemState:   
    def __init__(self, board):
        self.board = board
        try:
            self.empty, self.positions = self.createProblemState()
        except Invalid:
            print("This board is invalid")

    def getBoard(self):
        return self.board
    
    def updateBoard(self, move, step, remove = False):
        i, j = step
        self.board[i][j] = '.' if remove else move
            
    def createProblemState(self):
        empty = deque()
        positions = dict()
        
        for i in range(1, 10):
            positions[str(i)] = Positions()
            
        for i in range(9):
            for j in range(9):
                val = self.board[i][j]
                step = (i, j)
                if val == '.':
                    empty.append(step)
                else:
                    positions[val].addStep(step)
        return empty, positions
    
    def isComplete(self):
        return not self.empty

    def getNextStep(self):
        return self.empty[0]
    
    def getPossibleMoves(self, step):
        P = self.positions
        return [str(position + 1) for position in range(9) if P[str(position + 1)].validStep(step)]

    def makeMove(self, step, move):
        pos = self.positions[move]
        pos.addStep(step)
        self.updateBoard(move, step)
        self.empty.popleft()
        return self

    def undoMove(self, step, move):
        pos = self.positions[move]
        pos.removeStep(step)
        self.updateBoard(move, step, True)
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
        print(board)
        return None
        

test1 = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

solution = Solution()
solution.solveSudoku(test1)