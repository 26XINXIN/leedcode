class Solution:
    def __init__(self):
        self.s1 = None
        self.s2 = None
        self.s3 = None
        self.res = dict()

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        return self.interleave(0, 0, 0)
    
    def interleave(self, i, j, k):
        if i == len(self.s1) and j == len(self.s2) and k == len(self.s3):
            return True
        if (i, j, k) in self.res:
            return self.res[(i, j, k)]
        key = (i, j, k)
        
        if i == len(self.s1):
            while j < len(self.s2) and k < len(self.s3) and self.s2[j] == self.s3[k]:
                j += 1; k += 1           
            if j == len(self.s2) and k == len(self.s3):
                self.res[key] = True
                return True
            else:
                self.res[key] = False
                return False
        if j == len(self.s2):
            while i < len(self.s1) and k < len(self.s3) and self.s1[i] == self.s3[k]:
                i += 1; k += 1           
            if i == len(self.s1) and k == len(self.s3):
                self.res[key] = True
                return True
            else:
                self.res[key] = False
                return False
        
        while (i < len(self.s1) and j < len(self.s2) and k < len(self.s3) and 
            not (self.s1[i] == self.s3[k] and self.s2[j] == self.s3[k])):
            if self.s1[i] == self.s3[k]:
                i += 1; k += 1
            elif self.s2[j] == self.s3[k]:
                j += 1; k += 1
            else:
                self.res[key] = False
                return False
        
        if (i < len(self.s1) and j < len(self.s2) and k < len(self.s3) and 
            self.s1[i] == self.s3[k] and self.s2[j] == self.s3[k]):
            result = self.interleave(i + 1, j, k + 1) or self.interleave(i, j + 1, k + 1)
        else:
            result = self.interleave(i, j, k)
        self.res[key] = result
        return result


s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbbaccc"
result = Solution().isInterleave(s1, s2, s3)
print(result)