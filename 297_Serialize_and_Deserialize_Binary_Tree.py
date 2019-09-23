# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Codec:

    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     if not root:
    #         return []
    #     serial = list()
    #     q = Queue()
    #     q.put(root)
    #     while not q.empty():
    #         next_q = Queue()
    #         leaf = True
    #         while not q.empty():
    #             node = q.get()
    #             serial.append(node.val if node else None)
    #             if not node:
    #                 next_q.put(None)
    #                 next_q.put(None)
    #             else:
    #                 next_q.put(node.left)
    #                 next_q.put(node.right)
    #                 leaf = False
    #         if leaf: break
    #     return serial

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        layer = [root]
        data = []
        while layer:
            next_layer = []
            for node in layer:
                if node:
                    data.append(node.val)
                    next_layer.append(node.left)
                    next_layer.append(node.right)
                else:
                    data.append('null')
            layer = next_layer
        return data
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        root = TreeNode(data[0])
        layer = [root]
        idx = 1
        while layer:
            next_layer = list()
            for node in layer:
                if data[idx] != 'null':
                    node.left = TreeNode(data[idx])
                    next_layer.append(node.left)
                idx += 1
                if data[idx] != 'null':
                    node.right = TreeNode(data[idx])
                    next_layer.append(node.right)
                idx += 1
            layer = next_layer
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))