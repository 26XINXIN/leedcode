class Solution:
    def shortestPalindrome(self, s: str) -> str:
        idx = (len(s) + 1) // 2 
        while idx > 0: 
            if s[:idx] == s[idx:idx+idx:][::-1]:
                prefix = s[idx+idx:][::-1]
                break
            elif s[:idx] == s[idx-1:idx+idx-1:][::-1]:
                prefix = s[idx+idx-1:][::-1]
                break
            else:
                idx -= 1
        if idx == 0:
            return s[1:][::-1] + s
        return prefix + s