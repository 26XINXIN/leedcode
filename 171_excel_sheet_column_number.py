class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for c in s:
            d = ord(c) - ord("A") + 1
            n = n * 26 + d
        return n