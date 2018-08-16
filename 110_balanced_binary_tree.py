# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        if left_depth < 0 or right_depth < 0:
            return False
        elif abs(left_depth - right_depth) <= 1:
            return True
        else:
            return False
        
    def depth(self, root):
        if not root:
            return 0
        
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        if left_depth < 0 or right_depth < 0:
            return -100
        elif abs(left_depth - right_depth) <= 1:
            return max(left_depth, right_depth) + 1
        else:
            return -100