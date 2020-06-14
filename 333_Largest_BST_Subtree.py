# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def print_result(function):
    def wrapper(*args, **kwargs):
        root, lower, upper, nnodes = function(*args, **kwargs)
        print(root, lower, upper, nnodes)
        return root, lower, upper, nnodes

    return wrapper

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        bst, _, _, nnodes = self.findBST(root)
        return nnodes
    
    @print_result
    def findBST(self, root):
        if root.left is None and root.right is None:
            return root, root.val, root.val, 1
        elif root.left is None and root.right is not None:
            rightBST, rlower, rupper, rnnodes = self.findBST(root.right)
            if rightBST == root.right and rlower > root.val:
                return root, root.val, rupper, rnnodes + 1
            else:
                return rightBST, rlower, rupper, rnnodes
        elif root.right is None and root.left is not None:
            leftBST, llower, lupper, lnnodes = self.findBST(root.left)
            if leftBST == root.left and  lupper < root.val:
                return root, llower, root.val, lnnodes + 1
            else:
                return leftBST, llower, lupper, lnnodes
        else:
            rightBST, rlower, rupper, rnnodes = self.findBST(root.right)
            leftBST, llower, lupper, lnnodes = self.findBST(root.left)
            if rightBST == root.right and leftBST == root.left and lupper < root.val < rlower:
                return root, llower, rupper, rnnodes + lnnodes + 1
            else:
                if rnnodes > lnnodes:
                    return rightBST, rlower, rupper, rnnodes
                else:
                    return leftBST, llower, lupper, lnnodes