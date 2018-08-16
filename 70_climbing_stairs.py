class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Fabonacci
        ways = [0] * (n + 1)
        ways[0] = ways[1] = 1
        for i in range(2, n + 1):
            ways[i] = ways[i - 2] + ways[i - 1]
        return ways[n]