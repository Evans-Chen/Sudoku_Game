from collections import defaultdict, deque

fullContraintSet = {0, 1, 2, 3, 4, 5, 6, 7, 8}

class Constraint:
    def __init__(self):
        self.current = set()
        self.missing = fullContraintSet.copy()

    def swap(self, i, remove = False):
        if remove:
            self.current.remove(i)
            self.missing.add(i)
        else:
            self.missing.remove(i)
            self.current.add(i)

    def valid(self, i):
        return i in self.missing

class Positions:
    def __init__(self):
        self.row = Constraint()
        self.col = Constraint()
        self.grid = Constraint()
        
    def addStep(self, step):
        i, j = step
        grid = (i // 3) * 3 + (j // 3)
        self.row.swap(i)
        self.col.swap(j)
        self.grid.swap(grid)
        
    def removeStep(self, step):
        i, j = step
        grid = (i // 3) * 3 + (j // 3)
        self.row.swap(i, remove = True)
        self.col.swap(j, remove = True)
        self.grid.swap(grid, remove = True)       
        
    def validStep(self, step):
        i, j = step
        grid = (i // 3) * 3 + (j // 3)
        return self.row.valid(i) and self.col.valid(j) and self.grid.valid(grid)
    
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
        positions = dict()
        
        for i in range(1, 10):
            positions[str(i)] = Positions()
            
        for i in range(9):
            for j in range(9):
                val = self.board[i][j]
                step = (i, j)
                if val == '.': empty.append(step)
                else: positions[val].addStep(step)
        return empty, positions
    
    def isComplete(self):
        return not self.empty

    def getNextStep(self):
        return self.empty[0]
    
    def getPossibleMoves(self, step):
        P = self.positions
        return [str(position + 1) for position in range(9) if P[str(position + 1)].validStep(step)]

    def makeMove(self, step, move):
        self.positions[move].addStep(step)
        self.updateBoard(move, step)
        self.empty.popleft()
        return self

    def undoMove(self, step, move):
        self.positions[move].removeStep(step)
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