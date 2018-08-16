# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = list()
        level = [root]
        while len(level) > 0:
            next_level = list()
            for node in level:
                if not node.left == None:
                    next_level.append(node.left)
                if not node.right == None:
                    next_level.append(node.right)
            vals = list()
            for node in level:
                vals.append(node.val)
            result.append(vals)
            level = next_level
        result.reverse()
        return result