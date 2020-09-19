class Solution:
    def maxLength(self, arr: List[str]) -> int:
        char_to_word = dict()
        for word in arr:
            for c in word:
                char_to_word[c] = char_to_word.get(c, []) + [word]
        
        return self.fixConflict(char_to_word, [c for c in char_to_word if len(char_to_word[c]) > 1])
    
    def fixConflict(self, char_to_word, conflict_chars):
        if len(conflict_chars) == 0:
            return len([c for c in char_to_word if len(char_to_word[c]) == 1])
        
        n = 0
        while len(char_to_word[conflict_chars[n]]) <= 1:
            n += 1
        
        c = conflict_chars[n]
        words = list(char_to_word[c])

        max_len = 0
        
        for word in words:
            for word_char in word:
                char_to_word[word_char].remove(word)
        
        for word in words:
            
            for word_char in word:
                char_to_word[word_char].append(word)
            
            max_len = max(max_len, self.fixConflict(char_to_word, conflict_chars[n + 1 :]))
                
            for word_char in word:
                char_to_word[word_char].remove(word)

        return max_len
                    
            
            