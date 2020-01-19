# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        upper = None
        node = root
        while node:
            if node.val <= p.val:
                node = node.right
            elif node.val > p.val:
                upper = node if upper is None or node.val < upper.val else upper
                node = node.left
        return upper