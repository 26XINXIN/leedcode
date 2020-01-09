# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = self.order(root1)
        l2 = self.order(root2)
        i, j = 0, 0
        res = list()
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        while i < len(l1):
            res.append(l1[i])
            i += 1
        while j <= len(l2):
            res.append(l2[j])
            j += 1
        return res
    
    def order(self, tree):
        if not tree:
            return []
        else:
            return self.order(tree.left) + [tree.val] + self.order(tree.right)