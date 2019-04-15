class PrefixTreeNode:
    def __init__(self, char, parent, is_word):
        self.char = char
        self.parent = parent
        self.children = list()
        self.is_word = is_word
    
    def addChild(self, child):
        self.children.append(child)
    
    def findChild(self, char):
        for child in self.children:
            if child.char == char:
                return child
        return None

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = PrefixTreeNode('', None, False)

    def addPath(self, root, word):
        for char in word:
            root.addChild(PrefixTreeNode(char, root, False))
            root = root.children[-1]
        root.is_word = True

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root = self.root
        for i in range(len(word)):
            child = root.findChild(word[i])
            if not child:
                self.addPath(root, word[i:])
                return
            root = child
        root.is_word = True
        
    def findPath(self, word):
        nodes = [self.root]
        for char in word:
            children = list()
            for node in nodes:
                if char == '.':
                    children += node.children
                else:
                    child = node.findChild(char)
                    if child:
                        children.append(child)
            if not children:
                return None
            nodes = children
        return nodes

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        nodes = self.findPath(word)
        if not nodes:
            return False
        else:
            return any([node.is_word for node in nodes])
        

["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('at')
obj.addWord('and')
obj.addWord('an')
obj.addWord('add')
# print(obj.search('a'))
# print(obj.search('.at'))
obj.addWord('bat')
print(obj.search('.at'))
print(obj.search('an.'))
print(obj.search('a.d.'))
print(obj.search('b.'))
print(obj.search('a.d'))
print(obj.search('.'))