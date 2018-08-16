class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) != len(s2):
            return False

        return self.scrambled(s1, s2)
        
    def scrambled(self, s1, s2):
        print(s1 + "," + s2)
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        l = len(s1)
        if l == 1:
            return s1 == s2
        for mid in range(1, l):
            if (self.scrambled(s1[:mid], s2[:mid]) and self.scrambled(s1[mid:], s2[mid:]) 
            or self.scrambled(s1[:mid], s2[l - mid:]) and self.scrambled(s1[mid:], s2[:l - mid])):
                return True
        return False

print(Solution().isScramble("abb", "bab"))