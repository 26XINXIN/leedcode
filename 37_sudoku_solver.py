class Box:
    def __init__(self, i, j):
        self.i = i; self.j = j
        self.possible = list()
        self.filled = False
        self.num = ""

class Sudoku:
    def __init__(self, board):
        self.boxes = list()
        for i in range(9):
            self.boxes.append(list())
        for i in range(9):
            for j in range(9):
                self.boxes[i].append(Box(i, j))
                if board[i][j] != ".":
                    self.boxes[i][j].num = board[i][j]
                    self.boxes[i][j].filled = True

        


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
