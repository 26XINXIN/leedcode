class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-i-1] = s[-i-1], s[i]
        
        begin, end = 0, 0
        while end < len(s):
            while end < len(s) and s[end] != ' ':
                end += 1
            
            for i in range((end - begin) // 2):
                s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]
            
            begin, end = end + 1, end + 1