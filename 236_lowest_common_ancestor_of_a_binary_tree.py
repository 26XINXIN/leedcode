# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = self.search(root, p.val)
        path_q = self.search(root, q.val)
        i = 0
        while i < len(path_p) and i < len(path_q) and path_p[i].val == path_q[i].val:
            i += 1
        return path_p[i-1]
    
    def search(self, root, n):
        if root is None: return None
        if root.val == n:
            return [root]
        else:
            path = self.search(root.left, n) or self.search(root.right, n)
            if path is not None:
                return [root] + path
            else:
                return None