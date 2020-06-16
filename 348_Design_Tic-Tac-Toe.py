class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.grid = [[0] * n for _ in range(n)]
        self.row_sums = [0] * n
        self.col_sums = [0] * n
        self.diag_sums = [0, 0]
        self.row_nums = [0] * n
        self.col_nums = [0] * n
        self.diag_nums = [0, 0]
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.grid[row][col] = player
        self.row_sums[row] += player
        self.col_sums[col] += player
        self.row_nums[row] += 1
        self.col_nums[col] += 1
        if col == row:
            self.diag_sums[0] += player
            self.diag_nums[0] += 1
        if col + row == self.n - 1:
            self.diag_sums[1] += player
            self.diag_nums[1] += 1
        
        # print(self.__dict__)
        win_condition = player * self.n
        if self.row_nums[row] == self.n and self.row_sums[row] == win_condition:
            return player
        if self.col_nums[col] == self.n and self.col_sums[col] == win_condition:
            return player
        if any(self.diag_nums[i] == self.n and self.diag_sums[i] == win_condition for i in range(2)):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)