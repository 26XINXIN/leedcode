# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        
        idx = inorder.index(preorder[0])
        
        if idx != 0:
            left_inorder = inorder[:idx]
            l = len(left_inorder)
            left_preorder = preorder[1: 1 + l]
            root.left = self.buildTree(left_preorder, left_inorder)
        if idx != len(inorder) - 1:
            right_inorder = inorder[idx + 1:]
            l = len(right_inorder)
            right_preorder = preorder[-l:]
            root.right = self.buildTree(right_preorder, right_inorder)
        return root