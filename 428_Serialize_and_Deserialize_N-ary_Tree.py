"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from queue import Queue

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root is None:
            return ''
        code = str(root.val) + '\n'
        
        q = Queue()
        q.put(root)
        while not q.empty():
            next_q = Queue()
            layer_code = list()
            while not q.empty():
                node = q.get()
                node_code = list()
                for child in node.children:
                    next_q.put(child)
                    node_code.append(str(child.val))
                layer_code.append(','.join(node_code))
            
            code += '|'.join(layer_code) + '\n'
            q = next_q
        # print(code)
        return code
            
                

        
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if data == '':
            return None
        # print(data)
        layer_codes = data.split('\n')
        root = Node(val=layer_codes[0], children=[])
        layer_nodes = [root]
        for layer_code in layer_codes[1:]:
            if len(layer_code) == 0:
                break
            node_codes = layer_code.split('|')
            assert len(layer_nodes) == len(node_codes)
            next_layer_nodes = list()
            for node, node_code in zip(layer_nodes, node_codes):
                if len(node_code) == 0:
                    continue
                node_children = [int(child_val) for child_val in node_code.split(',')]
                
                for child_val in node_children:
                    child = Node(val=child_val, children=[])
                    node.children.append(child)
                    next_layer_nodes.append(child)
            layer_nodes = next_layer_nodes
        # print(self.serialize(root))
        return root

                    
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))