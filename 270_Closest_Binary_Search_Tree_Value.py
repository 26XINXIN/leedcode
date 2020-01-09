# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        node = root
        while node:
            if node.val == target:
                return node.val
            else:
                if abs(node.val - target) < abs(closest - target):
                    closest = node.val 
                if node.val > target:
                    node = node.left
                else:
                    node = node.right
        return closest
                