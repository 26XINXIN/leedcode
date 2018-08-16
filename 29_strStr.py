class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        # use KMP next time

        if len(haystack) == 0:
            return 0

        return haystack.index(needle)