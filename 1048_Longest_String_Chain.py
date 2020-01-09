class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: -len(x))
        max_length = i = 0
        while i < len(words) and len(words[i]) > max_length:
            word = words[i]
            for j in range(len(word)):
                subword = word[:j] + word[j+1:]