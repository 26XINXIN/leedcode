class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        paths = list()
        for _ in range(m):
            paths.append([0] * n)
        
        paths[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1 or paths[i-1][0] == 0:
                paths[i][0] = 0
            else:
                paths[i][0] = 1
        for j in range(1, n):
            if obstacleGrid[0][j] == 1 or paths[0][j-1] == 0:
                paths[0][j] = 0
            else:
                paths[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n): 
                if obstacleGrid[i][j] == 1 or obstacleGrid[i][j-1] == 1 and obstacleGrid[i-1][j] == 1:
                    paths[i][j] = 0
                elif obstacleGrid[i-1][j] == 1:
                    paths[i][j] = paths[i][j-1]
                elif obstacleGrid[i][j-1] == 1:
                    paths[i][j] = paths[i-1][j]
                else:
                    paths[i][j] = paths[i - 1][j] + paths[i][j -1]
        print(paths)
        return paths[m-1][n-1]

obstacleGrid = [[0,0,0], [0,1,0], [0,0,0]]
Solution().uniquePathsWithObstacles(obstacleGrid)