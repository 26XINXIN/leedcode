class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        left, right = 0, len(matrix) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid
        row = left

        from bisect import bisect_left

        i = bisect_left(matrix[row], target)
        if i != len(matrix[row]) and matrix[row][i] == target:
            return True
        else:
            return False
        
        