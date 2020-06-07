# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.search(root, 0)
        return root
        
    def search(self, root, gsum):
        if root.right is None:
            root.val += gsum
        else:
            gsum = self.search(root.right, gsum)
            root.val += gsum
        if root.left is not None:
            gsum = self.search(root.left, root.val)
            return gsum
        else:
            return root.val
            