# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        elif n == 1:
            return [TreeNode(1)]
        
        result = list()
        for x in range(1, n + 1):
            if x == 1:
                right_children = self.gen_SBT(2, n)
                for child in right_children:
                    root = TreeNode(1)
                    root.right = child
                    result.append(root)
            elif x == n:
                left_children = self.gen_SBT(1, n-1)
                for child in left_children:
                    root = TreeNode(n)
                    root.left = child
                    result.append(root)
            else:
                left_children = self.gen_SBT(1, x-1)
                right_children = self.gen_SBT(x+1, n)
                for r_child in right_children:
                    for l_child in left_children:
                        root = TreeNode(x)
                        root.left = l_child
                        root.right = r_child
                        result.append(root)
        return result
        
    def gen_SBT(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[TreeNode]
        returns the roots of BSTs
        """
        if left == right:
            return [TreeNode(left)]
        
        result = list()
        for x in range(left, right + 1):
            if x == left:
                right_children = self.gen_SBT(left + 1, right)
                for child in right_children:
                    root = TreeNode(left)
                    root.right = child
                    result.append(root)
            elif x == right:
                left_children = self.gen_SBT(left, right - 1)
                for child in left_children:
                    root = TreeNode(right)
                    root.left = child
                    result.append(root)
            else:
                left_children = self.gen_SBT(left, x-1)
                right_children = self.gen_SBT(x+1, right)
                for r_child in right_children:
                    for l_child in left_children:
                        root = TreeNode(x)
                        root.left = l_child
                        root.right = r_child
                        result.append(root)
        return result
                
        