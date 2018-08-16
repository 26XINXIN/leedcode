class TreeNode:
    def __init__(self, x):
        self.x = x
        self.children = dict()
        self.is_word = False

class Solution(object):

    def build_prefix_tree(self, wordDict):
        root = TreeNode(-1)
        for word in wordDict:
            i = 0
            it = root
            while i < len(word):
                if word[i] in it.children:
                    it = it.children[word[i]]
                    i += 1
                else:
                    break
            while i < len(word):
                node = TreeNode(word[i])
                it.children[word[i]] = node
                it = node
                i += 1
            it.is_word = True
        return root

    def search_word(self, s, root):
        i = 0
        it = root
        result = list()
        while it != None and i < len(s):
            if s[i] in it.children:
                it = it.children[s[i]]
                i += 1
                if it.is_word:
                    result.append(i)
            else:
                it = None
        return result


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # root = self.build_prefix_tree(wordDict)
        # return self.recursive_search(s, root)
        if len(wordDict) == 0:
            return False
        return self.dynamic_programming(s, wordDict)
        
    def recursive_search(self, s, root):
        if len(s) == 0:
            return True
        lengths = self.search_word(s, root)
        if len(lengths) == 0:
            return False
        for length in lengths[::-1]:
            if self.recursive_search(s[length:], root):
                return True
        return False


    def dynamic_programming(self, s, wordDict):
        dp = [False] * len(s)
        
        word_set = set(wordDict)
        min_len = min([len(word) for word in word_set])
        max_len = max([len(word) for word in word_set])

        i = 0
        while i < len(s):
            print(dp)
            for j in range(min_len, max_len + 1):
                if s[i:i + j] in word_set:
                    dp[i + j - 1] = True
                    if i + j == len(s):
                        return True
            
            k = 0
            while k < max_len + 1:
                if i + k < len(s) and dp[i + k] == True:
                    i = i + k + 1
                    break
                k += 1
            if k == max_len + 1:
                return False
            
        return False
            
                
Solution().dynamic_programming("ab", ["a", "b"])