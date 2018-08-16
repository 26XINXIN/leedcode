class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        n = len(board); m = len(board[0])
        alive = set()
        for i in range(n):
            if board[i][0] == "O":
                alive.add((i, 0))
            if board[i][m-1] == "O":
                alive.add((i, m-1))
        for j in range(m):
            if board[0][j] == "O":
                alive.add((0, j))
            if board[n-1][j] == "O":
                alive.add((n-1, j))
        
        try:
            from queue import Queue
        except:
            from Queue import Queue
        
        q = Queue()
        for loc in alive:
            q.put(loc)
        while not q.empty():
            i, j = q.get()
            if i != 0 and board[i-1][j] == "O" and (i-1, j) not in alive:
                alive.add((i-1, j)); q.put((i-1, j))
            if i != n-1 and board[i+1][j] == "O" and (i+1, j) not in alive:
                alive.add((i+1, j)); q.put((i+1, j))
            if j != 0 and board[i][j-1] == "O" and (i, j-1) not in alive:
                alive.add((i, j-1)); q.put((i, j-1))
            if j != m-1 and board[i][j+1] == "O" and (i, j+1) not in alive:
                alive.add((i, j+1)); q.put((i, j+1))
        
        for i in range(n):
            for j in range(m):
                if (i, j) in alive:
                    continue
                else:
                    board[i][j] = "X"