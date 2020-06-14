# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        robroot, robchildren = self.robery_amount(root)
        return robroot if robroot > robchildren else robchildren
    
    def robery_amount(self, root):
        if root is None:
            return 0, 0
        
        lroot, lnoroot = self.robery_amount(root.left)
        rroot, rnoroot = self.robery_amount(root.right)
        
        robroot = root.val + lnoroot + rnoroot
        robchildren = max(lroot, lnoroot) + max(rroot, rnoroot)
        
        return robroot, robchildren
        