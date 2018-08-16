class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = 0
        while n > 0:
            ones += n % 2
            n //= 2
        return ones