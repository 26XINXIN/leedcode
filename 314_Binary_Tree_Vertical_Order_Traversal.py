# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.col = {}
        layer = [(root, 0)]
        
        while layer:
            new_layer = []
            for node, c in layer:
                if c in self.col:
                    self.col[c].append(node.val)
                else:
                    self.col[c] = [node.val]
                if node.left: new_layer.append((node.left, c-1))
                if node.right: new_layer.append((node.right, c+1))
            layer = new_layer

        order = [n for _, n in sorted(self.col.items(), key=lambda x: x[0])]
        return order
    
    def search(self, root, c):
        if c in self.col:
            self.col[c].append(root.val)
        else:
            self.col[c] = [root.val]

        if root.left:
            self.search(root.left, c-1)
        if root.right:
            self.search(root.right, c+1)
