# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = list()
        self.it = root
        if not self.it: return
        while self.it.left:
            self.stack.append(self.it)
            self.it = self.it.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.it: 
            return False
        else:
            return True

    def next(self):
        """
        :rtype: int
        """
        result = self.it.val
        if self.it.right:
            jt = self.it.right
            while jt.left:
                self.stack.append(jt)
                jt = jt.left
            self.it = jt
        elif len(self.stack) > 0:
            self.it = self.stack.pop()
        else:
            self.it = None
        return result

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())