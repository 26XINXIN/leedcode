class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [[s]]
        result = list()
        for i in range(len(s)-1):
            if self.is_palindrome(s[:i+1]):
                sub_result = self.partition(s[i+1:])
                for r in sub_result:
                    result.append([s[:i+1]] + r)
        if self.is_palindrome(s):
            result.append([s])
        return result
    
    def is_palindrome(self, s):
        if len(s) == 1: return True
        i = 0; j = len(s)-1
        while i <= j:
            if s[i] == s[j]:
                i += 1; j -= 1
            else:
                return False
        return True