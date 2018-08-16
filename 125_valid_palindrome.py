class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        s = s.lower()
        i = 0; j = len(s)-1
        while i < j:
            while i < j and not self.valid(s[i]): i += 1
            while i < j and not self.valid(s[j]): j -= 1
            # print(s[i] + "," + s[j])
            if s[i] != s[j]: return False
            else: i += 1; j -= 1
        return True
    
    def valid(self, c):
        return c.isalpha() or c.isnumeric()