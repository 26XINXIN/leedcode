from collections import  Counter
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        cnt = Counter(s)
        if not self.canPermutePalindrome(cnt):
            return []
        
        if len(s) % 2 == 0:
            cnt = Counter({k: v // 2 for k, v in cnt.items()})
            self.odd_char = ''
        else:
            self.odd_char = ''
            for k, v in cnt.items():
                if v % 2 == 1:
                    self.odd_char = k
                    break
            cnt[self.odd_char] -= 1
            cnt = Counter({k: v // 2 for k, v in cnt.items() if v // 2 > 0})
        
        res = []
        self.half_len = len(s) // 2
        self.backTracking('', cnt, res)
        return res

    def backTracking(self, path, cnt, res):
        if len(path) == self.half_len:
            res.append(path + self.odd_char + path[::-1])
        else:
            for c in cnt:
                if cnt[c] != 0:
                    cnt[c] -= 1
                    path += c
                    self.backTracking(path, cnt, res)
                    path = path[:-1]
                    cnt[c] += 1
                

    def canPermutePalindrome(self, cnt) -> bool:
        odd_char = sum([v % 2 for v in cnt.values()])
        return odd_char <= 1