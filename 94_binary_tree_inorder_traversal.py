# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # return self.recursive_inorder_traversal(root)
        return self.iterative_traversal(root)


    def recursive_inorder_traversal(self, root):
        if root == None:
            return []

        return self.recursive_inorder_traversal(root.left) + [root.val] + self.recursive_inorder_traversal(root.right)

    def iterative_traversal(self, root): # TODO
        stack = list()
        result = list()
        stack.append(root)
        while len(stack) > 0:
            if stack[-1].left != None:
                it = stack[-1].left
            else:
                it = stack[-1]
                stack.pop()
                result.append(it.val)
                if it.right != None:
                    stack.append(it.right)
                continue
            while it.left != None:
                stack.append(it)
                it = it.left
            while len(stack) > 0 and stack[-1].right == None:
                result.append(stack[-1].val)
                stack.pop()
            if len(stack) > 0 and stack[-1].right != None:
                it = stack[-1]
                result.append(it.val)
                stack.append(it.right)
        return result
        
            