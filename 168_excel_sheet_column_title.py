class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title = ""
        while n > 0:
            n -= 1
            d = n % 26
            n //= 26
            title = chr(d + ord("A")) + title
        return title