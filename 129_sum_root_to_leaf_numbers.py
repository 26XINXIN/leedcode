# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.re_sum(root, 0)
        return self.result
    
    def re_sum(self, root, prefix):
        num = prefix * 10 + root.val
        if not root.right and not root.left:
            self.result += num
            return
        if root.right:
            self.re_sum(root.right, num)
        if root.left:
            self.re_sum(root.left, num)
        
        