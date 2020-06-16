class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 1: return 1
        elif n == 2: return 1
        elif n == 3: return 2
        elif n == 4: return 4
        elif n == 5: return 6
        
        k = n // 3
        r = n % 3
        if r == 0:
            return 3 ** k
        elif r == 1:
            return 3 ** (k - 1) * 4
        elif r == 2:
            return 3 ** k * 2