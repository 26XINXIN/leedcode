# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.max_paths = list()
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.generate_max_path(root)
        return max(self.max_paths)
    
    def generate_max_path(self, root):
        if not root.left and not root.right:
            self.max_paths.append(root.val)
            return root.val
        elif not root.left:
            r_max_path = self.generate_max_path(root.right)
            ret = root.val + r_max_path if r_max_path > 0 else root.val
            self.max_paths.append(ret)
            return ret
        elif not root.right:
            l_max_path = self.generate_max_path(root.left)
            ret = root.val + l_max_path if l_max_path > 0 else root.val
            self.max_paths.append(ret)
            return ret
        else:
            r_max_path = self.generate_max_path(root.right)
            l_max_path = self.generate_max_path(root.left)
            ret = max([root.val + r_max_path, root.val + l_max_path, root.val])
            self.max_paths.append(max(ret, root.val + l_max_path + r_max_path))
            return ret
