# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        diff, max_val, min_val = self.diff_max_min(root)
        return diff
    
    def diff_max_min(self, root):
        if root.left is None and root.right is None:
            return 0, root.val, root.val
        if root.left: 
            left_diff, left_max, left_min = self.diff_max_min(root.left)
        else:
            left_diff, left_max, left_min = None, None, None
        if root.right: 
            right_diff, right_max, right_min = self.diff_max_min(root.right)
        else:
            right_diff, right_max, right_min = None, None, None
        max_val = max([l for l in [left_max, right_max] if l is not None])
        min_val = min([l for l in [left_min, right_min] if l is not None])
        
        this_diff = max(abs(root.val-max_val), abs(root.val-min_val))
        diff = max([l for l in [this_diff, left_diff, right_diff] if l is not None])
        max_val = max(max_val, root.val)
        min_val = min(min_val, root.val)
        return diff, max_val, min_val
        