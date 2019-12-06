# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.n = 0
    
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.isUnivalue(root)
        return self.n
    
    def isUnivalue(self, root):
        if root.left is not None:
            leftUnival = self.isUnivalue(root.left)
        else:
            leftUnival = False
        if root.right is not None:
            rightUnival = self.isUnivalue(root.right)
        else:
            rightUnival = False

        if ((root.left is None or (leftUnival and root.val == root.left.val)) and 
            (root.right is None or (rightUnival and root.val == root.right.val))):
            self.n += 1
            # print(root, True)
            return True
        else:
            # print(root, False)
            return False