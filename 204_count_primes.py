class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        composite = [0] * n
        i = 2
        while i * i < n:
            j = i
            while i * j < n:
                composite[i * j] = 1
                j += 1
            i += 1
            while composite[i] == 1:
                i += 1
        return n - 2 - sum(composite)