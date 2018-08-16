class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if self.row_valid(board) and self.column_valid(board) and self.box_valid(board):
            return True
        else:
            return False

    def row_valid(self, board):
        for i in range(9):
            nums = list()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in nums:
                    return False
                else:
                    nums.append(board[i][j])
        return True

    def column_valid(self, board):
        for j in range(9):
            nums = list()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in nums:
                    return False
                else:
                    nums.append(board[i][j])
        return True

    def box_valid(self, board):
        for k in range(9):
            nums = list()
            x = k % 3
            y = k // 3
            i_range = range(3 * x, 3 * (x+1))
            j_range = range(3 * y, 3 * (y+1))
            for i in i_range:
                for j in j_range:
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in nums:
                        return False
                    else:
                        nums.append(board[i][j])
        return True