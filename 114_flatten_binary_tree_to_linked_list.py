# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        if not root.left and not root.right:
            return
        elif not root.left:
            self.flat(root.right)
        elif not root.right:
            left_last = self.flat(root.left)
            root.right = root.left
            root.left = None
        else:
            left = root.left
            right = root.right
            last_left = self.flat(root.left)
            last_right = self.flat(root.right)
            last_left.right = right
            root.right = left
            root.left = None
    
    def flat(self, root):
        if not root.left and not root.right:
            return root
        elif not root.left:
            return self.flat(root.right)
        elif not root.right:
            left_last = self.flat(root.left)
            root.right = root.left
            root.left = None
            return left_last
        else:
            left = root.left
            right = root.right
            last_left = self.flat(root.left)
            last_right = self.flat(root.right)
            last_left.right = right
            root.right = left
            root.left = None
            return last_right