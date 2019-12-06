class WordDistance:

    def __init__(self, words: List[str]):
        self.wordidx = dict()
        self.wordlen = len(words)
        for i, word in enumerate(words):
            self.wordidx[word] = self.wordidx.get(word, list()) + [i]
        

    def shortest(self, word1: str, word2: str) -> int:
        word1idx = self.wordidx[word1]
        word2idx = self.wordidx[word2]
        
        dis = self.wordlen
        for idx1 in word1idx:
            for idx2 in word2idx:
                dis = min(dis, abs(idx1 - idx2))
        
        return dis


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)