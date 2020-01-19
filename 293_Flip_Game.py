class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        res = list()
        for i in range(len(s)-1):
            if s[i] == s[i+1] == '+':
                res.append(s[:i-1] + '--' + s[i+2:])
        return res