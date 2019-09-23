class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern_word = dict()
        word_pattern = dict()
        words = str.split(' ')
        
        if len(pattern) != len(words):
            return False
        
        for p, word in zip(pattern, words):
            if p in pattern_word:
                if word != pattern_word[p] or word not in word_pattern or word_pattern[word] != p:
                    return False
            else:
                if word in word_pattern:
                    return False
                else:
                    pattern_word[p] = word
                    word_pattern[word] = p
        return True