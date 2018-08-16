# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        return self.is_sym(root.left, root.right)
    
    def is_sym(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False

        return p.val == q.val and self.is_sym(p.right, q.left) and self.is_sym(p.left, q.right)

        