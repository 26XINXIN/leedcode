class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[1])

        minute = -1
        
        rotted = list()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotted.append((i, j))
        
        
        def isFreshOrange(i, j):
            return 0 <= i < n and 0 <= j < m and grid[i][j] == 1

        while len(rotted) > 0:
            new_rotted = list()
            for i, j in rotted:
                if isFreshOrange(i - 1, j):
                    grid[i - 1][j] = 2
                    new_rotted.append((i - 1, j))
                if isFreshOrange(i + 1, j):
                    grid[i + 1][j] = 2
                    new_rotted.append((i + 1, j))
                if isFreshOrange(i, j - 1):
                    grid[i][j - 1] = 2
                    new_rotted.append((i, j - 1))
                if isFreshOrange(i, j + 1):
                    grid[i][j + 1] = 2
                    new_rotted.append((i, j + 1))
            minute += 1
            rotted = new_rotted
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return - 1
        return max(0, minute - 1)
            
        

        
        