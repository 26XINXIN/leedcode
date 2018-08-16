class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        foot_print = set()
        foot_print
        while n != 1 and n not in foot_print:
            foot_print.add(n)
            s = 0
            while n != 0:
                d = n%10
                s += d*d
                n //= 10
            n = s
        if n == 1:
            return True
        else:
            return False
                
        