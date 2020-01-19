class Solution:
    def __init__(self):
        self.win_cache = set()
        self.lose_cache = set()
    
    def canWin(self, s: str) -> bool:
        if s in self.win_cache:
            return True
        if not self.generatePossibleNextMoves(s):
            return False
        
        if any(self.willLose(_s) for _s in self.generatePossibleNextMoves(s)):
            self.win_cache.add(s)
            return True
        else:
            return False
    
    def willLose(self, s):
        if s in self.lose_cache:
            return True
        if not self.generatePossibleNextMoves(s):
            return True
        
        if all(self.canWin(_s) for _s in self.generatePossibleNextMoves(s)):
            self.lose_cache.add(s)
            return True
        else:
            return False

    def generatePossibleNextMoves(self, s: str) -> List[str]:
        res = list()
        for i in range(len(s)-1):
            if s[i] == s[i+1] == '+':
                res.append(s[:i] + '--' + s[i+2:])
        return res