class Solution:
    def __init__(self):
        pass

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.n = len(board)
        if not self.n:
            return []
        self.m = len(board[0])
        words = set(words)
        result = list()
        for word in words:
            if self.containsWord(word, board):
                result.append(word)
        return result
    
    def containsWord(self, word, board):
        if len(word) == 0:
            return True
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == word[0]:
                    if self.findPath(word[1:], board, {(i, j)}, (i, j)):
                        return True
        return False
    
    def findPath(self, word, board, path, current_position):
        print(path)
        if not word:
            return True
        valid_steps = self.findValidStep(board, path, current_position)
        for i, j in valid_steps:
            if board[i][j] == word[0]:
                new_path = set(path)
                new_path.add((i, j))
                if self.findPath(word[1:], board, new_path, (i, j)):
                    return True
        return False
    
    def findValidStep(self, board, path, current_position):
        i, j = current_position
        valid_steps = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        valid_steps = [s for s in valid_steps if s not in path]
        valid_steps = filter(lambda pos: (0 <= pos[0] < self.n and 0 <= pos[1] < self.m), valid_steps)
        return valid_steps

board = [
    ["b","a","a","b","a","b"],
    ["a","b","a","a","a","a"],
    ["a","b","a","a","a","b"],
    ["a","b","a","b","b","a"],
    ["a","a","b","b","a","b"],
    ["a","a","b","b","b","a"],
    ["a","a","b","a","a","b"]]
words = ["aabbbbabbaababaaaabababbaaba"]
#,"abaabbbaaaaababbbaaaaabbbaab","ababaababaaabbabbaabbaabbaba"]

print(Solution().findWords(board, words))
