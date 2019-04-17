class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        for i in range(n):
            j = 0
            while j < m:
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    break
                else:
                    j += 1
        return False

class Solution1:
    def __init__(self):
        self.n = 0
        self.m = 0

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.n = len(matrix)
        if self.n == 0:
            return False
        self.m = len(matrix[0])
        return self.search_partial_matrix(matrix, target, 0, 0)
    
    def search_partial_matrix(self, matrix, target, i, j):
        if i == self.n or j == self.m:
            return False
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            return False
        else:
            return (self.search_partial_matrix(matrix, target, i+1, j) or 
                    self.search_partial_matrix(matrix, target, i, j+1)) 

            