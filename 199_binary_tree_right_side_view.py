# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        q = Queue()
        q.put(root)
        result = list()
        while not q.empty():
            new_q = Queue()
            while not q.empty():
                node = q.get()
                if node.left:
                    new_q.put(node.left)
                if node.right:
                    new_q.put(node.right)
            result.append(node.val)
            q = new_q
        return result