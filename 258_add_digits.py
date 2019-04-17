class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) > 1:
            num = str(sum(int(c) for c in num))
        return int(num)