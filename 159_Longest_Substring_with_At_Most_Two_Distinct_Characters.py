from collections import Counter

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        i, j = 0, 0
        wcnt = Counter()
        maxLen = 0
        while j < len(s):
            if len(wcnt) < 2 or s[j] in wcnt:
                wcnt[s[j]] += 1
                
            else:
                while len(wcnt) == 2:
                    wcnt[s[i]] -= 1
                    if wcnt[s[i]] == 0:
                        del wcnt[s[i]]
                    i += 1
                wcnt[s[j]] += 1
            j += 1
            maxLen = max(maxLen, j - i)
        
        return maxLen
                    
                
