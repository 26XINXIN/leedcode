class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        dist = list()
        for i in range(len(wordList) + 2):
            dist.append([0] * (len(wordList) + 2))
        wordList.append(beginWord)
        wordList.append(endWord)
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                dist[i][j] = self.distance(wordList[i], wordList[j])
        
        path = dict()
        inserted = set([len(wordList)-2])
        new = list([len(wordList)-2])
        while len(inserted) < len(wordList):
            new_new = list()
            for i in new:
                for j in len(dist[i]):
                    if len[i][j] == 1 and j not in inserted:
                        new
        
                        
        
        
    def distance(self, w1, w2):
        if len(w1) != len(w2):
            return -1
        d = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]: d+=1
        return d