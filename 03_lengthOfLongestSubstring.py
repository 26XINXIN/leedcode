class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        sub = ""
        for i in range(0, len(s)):
            ind = sub.find(s[i])
            if ind == -1:
                sub += s[i]
            else:
                sub = sub[ind + 1:] + s[i]
            longest = max(longest, len(sub))
        return longest
