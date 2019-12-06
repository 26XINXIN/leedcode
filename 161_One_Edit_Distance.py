class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return False
        if abs(len(s) - len(t)) > 1:
            return False
        if s == t:
            return False
        
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                if len(s) > len(t):
                    return i + 1 == len(s) or s[i+1:] == t[j:]
                elif len(s) < len(t):
                    return j + 1 == len(t) or s[i:] == t[j+1:]
                else:
                    return (j + 1 == len(t) and i + 1 == len(s)) or s[i+1:] == t[j+1:]
        return True