# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        newRoot = root
        while newRoot.left:
            newRoot = newRoot.left
        
        self.upsideDown(root, root.left, root.right)
        root.left = None
        root.right = None
        return newRoot
    
    def upsideDown(self, root, left, right):
        if left is None: return
        self.upsideDown(left, left.left, left.right)
        if right:
            self.upsideDown(right, right.left, right.right)
        left.right = root
        left.left = right