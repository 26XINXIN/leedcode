class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        paths = list()
        for _ in range(m):
            paths.append([0] * n)

        paths[0][0] = grid[0][0]
        for i in range(1, m):
            paths[i][0] = paths[i - 1][0] + grid[i][0]
        for j in range(1, n):
            paths[0][j] = paths[0][j - 1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = min(paths[i-1][j], paths[i][j-1]) + grid[i][j]
        
        return paths[m-1][n-1]