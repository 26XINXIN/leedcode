# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            if sum == 0:
                return True
            else:
                return False
        elif not root.right and not root.left:
            return sum == root.val
        elif not root.right:
            return self.hasPathSum(root.left, sum - root.val)
        elif not root.left:
            return self.hasPathSum(root.right, sum - root.val)
        else:
            sub_sum = sum - root.val
            return self.hasPathSum(root.right, sub_sum) or self.hasPathSum(root.left, sub_sum)