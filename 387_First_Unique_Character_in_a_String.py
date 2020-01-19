class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = dict()
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1