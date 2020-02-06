# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.length = 1
        
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.search(root)
        return self.length

    def search(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return 1
        
        l = 1
        if root.left is not None:
            ll = self.search(root.left)
            if root.val + 1 == root.left.val:
                l = max(l, ll + 1)
        if root.right is not None:
            rl = self.search(root.right)
            if root.val + 1 == root.right.val:
                l = max(l, rl + 1)
        self.length = max(self.length, l)
        # print(root.val, l)
        return l