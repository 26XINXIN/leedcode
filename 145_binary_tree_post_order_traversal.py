# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.iterative_postorder_traversal(root)
        
        # left = self.postorderTraversal(root.left)
        # right = self.postorderTraversal(root.right)
        # return left + right + [root.val]

    def iterative_postorder_traversal(self, root):
        result = list()
        stack = list()
        stack.append(root)
        while len(stack) > 0:
            root = stack.pop()
            result.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return result[::-1]