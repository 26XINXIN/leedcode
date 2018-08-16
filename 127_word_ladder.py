class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
            begin_index = len(wordList) - 1
        else:
            begin_index = wordList.index(beginWord)
        end_index = wordList.index(endWord)
        
        # initiate transfer matrix
        P = list()
        for _ in range(len(wordList)):
            P.append([0] * len(wordList))
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.reachable(wordList[i], wordList[j]):
                    P[i][j] = P[j][i] = 1

        transfer = 1
        from copy import deepcopy
        Pn = deepcopy(P)
        while Pn[begin_index][end_index] != 1:
            Pn = self.dot(Pn, P)
            transfer += 1
        return transfer
    
    def dot(self, p1, p2):
        p = list()
        for _ in range(len(p1)):
            p.append([0] * len(p1))
        for i in range(len(p1)):
            for j in range(len(p2)):
                for k in range(len(p1)):
                    if p1[i][k] * p2[k][j] == 1:
                        p[i][j] = 1
                        break
        return p

    def reachable(self, w1, w2):
        if len(w1) != len(w2):
            return False
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
        if diff == 1:
            return True
        else:
            return False