class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        all_is_space = True
        for c in s:
            if c != " ":
                all_is_space = False
        if all_is_space:
            return 0

        length = 0
        pos = len(s) - 1
        while length == 0:
            length = pos
            pos = s.rfind(" ", 0, pos + 1)
            length = length - pos 
            pos -= 1
            
        return length
        