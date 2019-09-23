class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        newborn = 2
        death = 3
        alive = 1
        dead = 0

        if len(board) == 0 or len(board[0]) == 0: return
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                state = board[i][j]
                n_neigh = 0
                for x, y in self.neighbors(i, j, n, m):
                    if 0 <= x < n and 0 <= y < m:
                        n_neigh += int(board[x][y] == alive or board[x][y] == death)
                if state == alive:
                    if 2 <= n_neigh <= 3:
                        pass # alive
                    else:
                        board[i][j] = death
                else:
                    if n_neigh == 3:
                        board[i][j] = newborn
                    else:
                        pass # death
        
        for i in range(n):
            for j in range(m):
                board[i][j] = int(board[i][j] == alive or board[i][j] == newborn)
    
    def neighbors(self, i, j, n, m):
        # if i == 0 and j == 0:
        #     return [(1, 0), (0, 1), (1, 1)]
        # elif i == 0 and j == m-1:
        #     return [(1, j), (0, j-1), (1, j-1)]
        # elif i == n-1 and j == 0:
        #     return [(i, 1), (i-1, 0), (i-1, 1)]
        # elif i == n and j == m:
        #     return [(n-1, m), (n, m-1), (n-1, m-1)]
        # elif i == 0:
        #     return [(0, j-1), (0, j+1), (1, j-1), (1, j), (1, j+1)]
        # elif i == n-1:
        #     return [(i, j-1), (i, j+1), (i-1, j-1), (i-1, j), (i-1, j+1)]
        # elif j == 0:
        #     return [(i-1, 0), (i+1, 0), (i-1, 1), (i, 1), (i+1, 1)]
        # elif j == m-1:
        #     return [(i-1, j), (i+1, j), (i-1, j-1), (i, j-1), (i+1, j-1)]
        # else:
        return [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]


m = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(m)
print(m)