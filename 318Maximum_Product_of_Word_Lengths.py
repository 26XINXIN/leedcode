class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if len(words) == 0:
            return 0
        bitmasks = [[0] * 26 for _ in range(len(words))]
        for word, bitmask in zip(words, bitmasks):
            for c in word:
                bitmask[ord(c) - ord('a')] = 1
        
        max_product = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                same_char = False
                for k in range(26):
                    if bitmasks[i][k] == 1 and bitmasks[j][k] == 1:
                        same_char = True
                        break
                if same_char:
                    continue
                max_product = max(max_product, len(words[i]) * len(words[j]))
        
        return max_product
        