class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1/x
        elif n == 0:
            return 1
        elif x == 0:
            return 0
        return self.recursive_pow(x, n)

    def recursive_pow(self, x, n):
        if n == 1:
            return x
        half = self.recursive_pow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x