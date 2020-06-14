import bisect

class TrieNode():
    def __init__(self, val, index=None):
        self.val = val
        self.index = None
        self.children = []
    
    def __le__(self, node):
        return self.val <= node.val
    
    def __lt__(self, node):
        return self.val < node.val

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        self.trie = TrieNode('')
        for i, w in enumerate(words):
            self.insert_path(w[::-1], i)
        
        all_pairs = list()
        for i, w in enumerate(words):
            pairs = self.search_path(w, i)
            all_pairs.extend(pairs)
        return all_pairs
    
    def insert_path(self, word, index):
        it = self.trie
        i = 0
        while i < len(word):
            node = TrieNode(word[i])
            loc = bisect.bisect_left(it.children, node)
            if loc != len(it.children) and it.children[loc].val == word[i]:
                it = it.children[loc]
                i += 1
            else:
                it.children.insert(loc, node)
                i += 1
                it = node
        it.index = index
    
    def search_path(self, word, index):
        it = self.trie
        i = 0
        pairs = list()
        while i < len(word):
            if it.index is not None and self.is_palindrome(word[i:]):
                    pairs.append([index, it.index])
            if len(it.children) == 0:
                it = None
                break
            node = TrieNode(word[i])
            loc = bisect.bisect_left(it.children, node)
            if loc != len(it.children) and it.children[loc].val == word[i]:
                it = it.children[loc]
                i += 1
            else:
                break
        if it is not None and i == len(word):
            if it.index is not None:
                pairs.append([index, it.index])
            for child in it.children:
                possible_subwords = self.find_subwords(child)
                for word, windex in possible_subwords:
                    if index != windex and self.is_palindrome(word):
                        pairs.append([index, windex])
        return pairs
    
    def is_palindrome(self, w):
        if len(w) == 0: return True
        for i in range(len(w) // 2):
            if w[i] != w[-i - 1]:
                return False
        return True
    
    def find_subwords(self, trie):
        words = list()
        if trie.index is not None:
            words.append((trie.val, trie.index))
        for child in trie.children:
            sub_words = self.find_subwords(child)
            for sw, idx in sub_words:
                words.append((trie.val + sw, idx))
        return words
            
            
        