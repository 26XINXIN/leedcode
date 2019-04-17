from typing import List
class Solution:
    def __init__(self):
        self.n = 0
        self.m = 0
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.n = len(matrix)
        if self.n == 0:
            return 0
        self.m = len(matrix[0])
        
        max_sq = 1
        for i in range(self.n):
            for j in range(self.m):
                max_sq = max(self.max_square(matrix, i, j), max_sq)
        return max_sq
    
    def max_square(self, matrix, row, col):
        sq_len = 0
        while True:
            if row + sq_len >= self.n or col + sq_len >= self.m:
                break
            for i in range(row, row + sq_len + 1):
                if matrix[i][col + sq_len] != '1':
                    zero = True
                    break
            if zero: break
            for j in range(col, col + sq_len + 1):
                if matrix[row + sq_len][j] != '1':
                    zero = True
                    break
            if zero: break
            sq_len += 1
        return sq_len * sq_len
            