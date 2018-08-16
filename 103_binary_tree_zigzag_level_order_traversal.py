# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = list()
        level = [root]
        left = True
        while len(level):
            next_level = list()
            if left:
                for i in range(len(level) - 1, -1, -1):
                    if level[i].right != None:
                        next_level.append(level[i].right)
                    if level[i].left != None:
                        next_level.append(level[i].left)
                left = False
            else:
                for i in range(len(level) - 1, -1, -1):
                    if level[i].left != None:
                        next_level.append(level[i].left)
                    if level[i].right != None:
                        next_level.append(level[i].right)
                left = True
            vals = list()
            for node in level:
                vals.append(node.val)
            result.append(vals)
            level = next_level
        return result