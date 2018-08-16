try:
    from queue import Queue
except:
    from Queue import Queue

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        begin_node = UndirectedGraphNode(node.label)
        label_to_node = dict()
        label_to_node[begin_node.label] = begin_node

        q = Queue()
        for neigh in node.neighbors:
            if neigh.label == begin_node.label:
                begin_node.neighbors.append(begin_node)
            else:
                q.put(neigh)
        while not q.empty():
            node = q.get()
            cloned_node = UndirectedGraphNode(node.label)
            label_to_node[cloned_node.label] = cloned_node
            for neigh in node.neighbors:
                if neigh.label in label_to_node:
                    cloned_node.neighbors.append(label_to_node[neigh.label])
                    if cloned_node.label != neigh.label:
                        label_to_node[neigh.label].neighbors.append(cloned_node)
                else:
                    q.put(neigh)
        
        return begin_node

            
node = UndirectedGraphNode(0)
node.neighbors.append(node)
node.neighbors.append(node)
cloned = Solution().cloneGraph(node)
