class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        i = 0
        i = self.is_valid_subtree(preorder, i)
        if i == -1 or i < len(preorder):
            return False
        return True
    
    def is_valid_subtree(self, preorder, i):
        if i >= len(preorder):
            return -1
        if preorder[i] == '#':
            return i + 1
        else:
            i = self.is_valid_subtree(preorder, i + 1)
            if i == -1:
                return - 1
            i = self.is_valid_subtree(preorder, i)
            if i == -1:
                return - 1
            return i