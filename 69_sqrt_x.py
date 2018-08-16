class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        elif x == 1: return 1
        left = 0; right = x
        while left < right-1:
            middle = (left + right) // 2
            sq = middle * middle
            if sq == x:
                return middle
            elif sq < x:
                left = middle
            else:
                right = middle
        return left
            