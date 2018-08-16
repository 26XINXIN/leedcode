# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        layer = [root]
        while len(layer) > 0:
            next_layer = list()
            for node in layer:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            for i in range(len(layer) - 1):
                layer[i].next = layer[i+1]
            layer = next_layer
        