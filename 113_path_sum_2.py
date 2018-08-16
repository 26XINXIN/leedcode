# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return False
        result = list()
        self.findPath(root, [], sum, result)
        return result
        
    def findPath(self, root, prefix, sum, result):
        prefix.append(root.val)
        sum = sum - root.val
        if not root.left and not root.right:
            if sum == 0:
                r = list(prefix)
                result.append(r)
        elif not root.left:
            self.findPath(root.right, prefix, sum, result)
        elif not root.right:
            self.findPath(root.left, prefix, sum, result)
        else:
            self.findPath(root.right, prefix, sum, result)
            self.findPath(root.left, prefix, sum, result)
        prefix.pop()
