import bisect

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = list()
        self.is_word = False

    def __lt__(self, x):
        return self.val < x.val

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode("")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        i = 0
        it = self.root
        while i < len(word):
            if len(it.children) > 0:
                k = bisect.bisect_left(it.children, TreeNode(word[i]))
                if k < len(it.children) and it.children[k].val == word[i]:
                    it = it.children[k]
                    i += 1
                else:
                    break
            else:
                break
        # haven't a prefix
        if i < len(word):
            while i < len(word):
                jt = TreeNode(word[i])
                if len(it.children) > 0:
                    bisect.insort_left(it.children, jt)
                else:
                    it.children.append(jt)
                it = jt
                i += 1
        it.is_word = True
         

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        i = 0
        it = self.root
        while i < len(word):
            if len(it.children) > 0:
                k = bisect.bisect_left(it.children, TreeNode(word[i]))
                if k < len(it.children) and it.children[k].val == word[i]:
                    it = it.children[k]
                    i += 1
                else:
                    break
            else:
                break
        if i != len(word) or not it.is_word:
            return False
        else:
            return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        i = 0
        it = self.root
        while i < len(prefix):
            if len(it.children) > 0:
                k = bisect.bisect_left(it.children, TreeNode(prefix[i]))
                if k < len(it.children) and it.children[k].val == prefix[i]:
                    it = it.children[k]
                    i += 1
                else:
                    break
            else:
                break
        if i == len(prefix):
            return True
        else:
            return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)