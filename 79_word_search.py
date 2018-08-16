# from copy import deepcopy

class Solution:
    def __init__(self):
        self.board = None
        self.word = None
        self.n = None
        self.m = None
        self.blocked = None
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.n = len(board)
        if self.n == 0: return False
        self.m = len(board[0])
        start = list()
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == word[0]:
                    start.append((i, j))
        self.blocked = list()
        for i in range(self.n):
            self.blocked.append([0] * self.m)
        self.board = board
        self.word = word
        blocked = list()
        for i in range(self.n):
            blocked.append([0] * self.m)
        for i, j in start:
            if self.search(i, j, 0):
                return True
        return False

    def search(self, i, j, l):
        l += 1
        if l == len(self.word):
            return True
        # blocked = deepcopy(pre_blocked)
        self.blocked[i][j] = 1
        
        directions = self.get_directions(i, j)
        if len(directions) == 0:
            self.blocked[i][j] = 0
            return False
        # print("{}, {}".format(i, j))
        # print(directions)
        for i, j in directions:
            if self.blocked[i][j] == 0 and self.board[i][j] == self.word[l] and self.search(i, j, l):
                return True
        self.blocked[i][j] = 0
        return False

    def get_directions(self, i, j):
        left, right, up, down = True, True, True, True
        if i == 0:        up = False
        if i == self.n-1: down = False
        if j == 0:        left = False
        if j == self.m-1: right = False
        dirs = list()
        if up: dirs.append((i-1, j))
        if down: dirs.append((i+1, j))
        if left: dirs.append((i, j-1))
        if right: dirs.append((i, j+1))
        return dirs
        


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
result = Solution().exist(board, word)
print(result)
