# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        r = self.check_valid(root)
        if r == None:
            return False
        return True
    
    def check_valid(self, root):
        if root.left == None and root.right == None:
            return [root.val, root.val]
        elif root.left == None:
            r = self.check_valid(root.right)
            if r == None or root.val >= r[0]:
                return None
            else:
                return [root.val, r[1]]
        elif root.right == None:
            l = self.check_valid(root.left)
            if l == None or root.val <= l[1]:
                return None
            else:
                return [l[0], root.val]
        else:
            r = self.check_valid(root.right)
            l = self.check_valid(root.left)
            if r == None or l == None or root.val <= l[1] or root.val >= r[0]:
                return None
            else:
                return [l[0], r[1]]