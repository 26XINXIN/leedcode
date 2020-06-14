class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i, j = 0, 0
        chars = dict()
        max_len = 0
        while j < len(s):
            chars[s[j]] = chars.get(s[j], 0) + 1
            while len(chars) > k:
                chars[s[i]] -= 1
                if chars[s[i]] == 0:
                    chars.pop(s[i])
                i += 1
            j += 1
            max_len = max(max_len, j - i)
        return max_len