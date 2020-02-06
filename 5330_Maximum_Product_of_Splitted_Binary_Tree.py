# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.sum_total = self.sumTree(root)
        self.maxp = 0
        self.split(root)
        return self.maxp % (1000000000 + 7)
    
    def split(self, root):
        sum_left = sum_right = 0
        if root.left:
            sum_left = self.split(root.left)
        if root.right:
            sum_right = self.split(root.right)
        self.maxp = max([self.maxp, sum_left * (self.sum_total - sum_left), sum_right * (self.sum_total - sum_right)])
        return root.val + sum_right + sum_left
            
    
    def sumTree(self, root):
        if root == None:
            return 0
        return self.sumTree(root.left) + self.sumTree(root.right) + root.val
        