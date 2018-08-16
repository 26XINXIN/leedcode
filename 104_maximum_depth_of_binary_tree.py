# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        level = [root]
        depth = 0
        while len(level) > 0:
            next_level = list()
            for node in level:
                if node.left != None:
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)
            level = next_level
            depth += 1
        return depth