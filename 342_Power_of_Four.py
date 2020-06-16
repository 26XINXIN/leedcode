class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        k = 1
        while k < num:
            k *= 4
        return k == num