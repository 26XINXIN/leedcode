# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = list()
        stack.append(root)
        i = 0
        while len(stack) > 0:
            node = stack[-1].left
            while node: 
                stack.append(node)
                node = node.left
            node = stack.pop()
            i += 1
            # print(i, node.val)
            if i == k: return node.val
            while not node.right and len(stack) > 0:
                node = stack.pop()
                i += 1
                # print(i, node.val)
                if i == k: return node.val
            if node.right:
                stack.append(node.right)