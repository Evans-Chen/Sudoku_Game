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
        
        for i in range(1,10):
            self.positions[i] = Positions()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (board[row][col] != "."):
                    self.positions[int(board[row][col])].add(row, col) 
                else:
                    self.emptyCells.append((row,col))
        
        board = self.solveWithBacktracking(board)
        
        
    def solveWithBacktracking(self,board):
        if self.isComplete():
            return board
        nextStep = self.emptyCells[0]
        for move in ["1","2","3","4","5","6","7","8","9"]:
            # Sometimes it's easier to make a move, then check if it's valid.
            # Sometimes it's easier to check if a move is valid first.
            # Just make sure that you always undo a move properly!
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
                if (board[row][col] == "."):
                    return ((row,col))
    
    def isValid(self, board, nextStep, move):
        if nextStep[0] in self.positions[move].row: return False
        if nextStep[1] in self.positions[move].col: return False
        if (nextStep[0]//3)*3+(nextStep[1]//3) in self.positions[move].grid: return False
        return True
    
    def makeMove(self, board, nextStep, move):
        board[nextStep[0]][nextStep[1]] = move
        self.positions[int(move)].add(nextStep[0],nextStep[1])
        self.emptyCells.pop(0)
        return board
    
    def undoMove(self, board, nextStep, move):
        board[nextStep[0]][nextStep[1]] = "."
        self.positions[int(move)].delete(nextStep[0],nextStep[1])
        self.emptyCells.insert(0,nextStep)
        return board
    
