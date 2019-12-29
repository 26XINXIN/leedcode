from collections import Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        letters = Counter()
        substrings = Counter()

        for i in range(len(s) - minSize + 1):
            letters = Counter(s[i:i+minSize])
            if len(letters) <= maxLetters:
                print(s[i:i+minSize])
                substrings[s[i:i+minSize]] += 1
            else:
                continue
            for j in range(i + minSize + 1, min(len(s), i + maxSize + 1)):
                letters[s[j]] += 1
                if len(letters) <= maxLetters:
                    print(s[i:j])
                    substrings[s[i:j]] += 1
                else:
                    break
        print(substrings)
        return max(substrings.values()) if len(substrings) > 0 else 0
         

res = Solution().maxFreq("abcde", 2, 3, 3)
print(res)