class Solution(object):
    def minCut(self, s):
        cache = set()
        min_cut_list = [-1] * len(s)
        for i in range(len(s)):
            if s[:i+1] in cache:
                min_cut_list[i] = 0
            elif self.is_palindrome(s[:i+1]):
                cache.add(s[:i+1])
                min_cut_list[i] = 0
            else:
                ans = len(s)
                for j in range(i):
                    if s[j+1:i+1] in cache:
                        ans = min(ans, min_cut_list[j] + 1)
                    elif self.is_palindrome(s[j+1:i+1]):
                        cache.add(s[i+1:j+1])
                        ans = min(ans, min_cut_list[j] + 1)
                min_cut_list[i] = ans
        return min_cut_list[-1]
            

    def recursive_minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 0
        if self.is_palindrome(s):
            return 0
        cuts = list()
        for i in range(len(s)-1):
            if self.is_palindrome(s[:i+1]):
                cuts.append(self.minCut(s[i+1:]) + 1)
        return min(cuts)
        

    def is_palindrome(self, s):
        if len(s) == 1: return True
        i = 0; j = len(s)-1
        while i <= j:
            if s[i] == s[j]:
                i += 1; j -= 1
            else:
                return False
        return True