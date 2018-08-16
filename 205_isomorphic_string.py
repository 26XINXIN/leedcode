class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pattern_s = self.get_pattern(s)
        pattern_t = self.get_pattern(t)
        return pattern_s == pattern_t

    def get_pattern(self, s):
        pattern = ""
        mapping = dict()
        for i in range(len(s)):
            if s[i] in mapping:
                pattern += mapping[s[i]]
            else:
                mapping[s[i]] = str(chr(ord("A") + len(mapping)))
                pattern += mapping[s[i]]
        return pattern