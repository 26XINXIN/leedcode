# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        
        if idx != 0:
            left_inorder = inorder[:idx]
            left_postorder = postorder[:idx]
            root.left = self.buildTree(left_inorder, left_postorder)
        if idx != len(inorder) - 1:
            right_inorder = inorder[idx + 1:]
            right_postorder = postorder[idx:-1]
            root.right = self.buildTree(right_inorder, right_postorder)
        return root
            