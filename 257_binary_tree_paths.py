# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        val = str(root.val)
        paths = list()
        if root.left is not None:
            paths += [val + '->' + p for p in self.binaryTreePaths(root.left)]
        if root.right is not None:
            paths += [val + '->' + p for p in self.binaryTreePaths(root.right)]
        return paths
        