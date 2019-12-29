from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = Counter(s)
        odd_char = sum([v % 2 for v in cnt.values()])
        return odd_char <= 1
        