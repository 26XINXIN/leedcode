class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        wordidx = dict()
        for i, word in enumerate(words):
            wordidx[word] = wordidx.get(word, list()) + [i]
        
        word1idx = wordidx[word1]
        word2idx = wordidx[word2]
        
        dis = len(words)
        for idx1 in word1idx:
            for idx2 in word2idx:
                if word1 == word2 and idx1 == idx2:
                    continue
                dis = min(dis, abs(idx1 - idx2))
        
        return dis