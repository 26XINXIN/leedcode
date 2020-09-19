class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n = len(board)
        if n == 0:
            return 0
        m = len(board[0])
        if m == 0:
            return 0

        ships = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X':
                    ships += 1
                    board[i][j] == '.'
                    if (0 <= i - 1 < n and board[i - 1][j] == 'X') or (0 <= i + 1 < n and board[i + 1][j] == 'X'):
                        ii = i - 1
                        while 0 <= ii < n and board[ii][j] == 'X':
                            board[ii][j] = '.'
                            ii -= 1
                        ii = i + 1
                        while 0 <= ii < n and board[ii][j] == 'X':
                            board[ii][j] = '.'
                            ii += 1
                    else:
                        jj = j - 1
                        while 0 <= jj < m and board[i][jj] == 'X':
                            board[i][jj] = '.'
                            jj -= 1
                        jj = j + 1
                        while 0 <= jj < m and board[i][jj] == 'X':
                            board[i][jj] = '.'
                            jj += 1
        return ships
