class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        fives = 0
        while n > 0:
            n //= 5
            fives += n
        return fives