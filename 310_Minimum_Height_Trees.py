# wrong direction: longest path / 2

import heapq

class Solution:
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.children = []
            self.height = 1   

        def __le__(self, node):
            return -self.height <= -node.height
        
        def __lt__(self, node):
            return -self.height < -node.height
            
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        root = self.constructTree(edges, 0)
        
        if len(root.children) == 1:
            node = root.children.pop()
            root.height = 1
            heapq.heappush(node.children, root) 
            root = node

        maxchild = heapq.heappop(root.children)
        rootheight = root.children[0].height + 1
        while rootheight + 1 < maxchild.height:
            # print(root.val)
            root.height = rootheight
            heapq.heappush(root)
            maxchild = heapq.heappop(root.children)
            rootheight = root.children[0].height + 1
        heapq.heappush(root.children, maxchild)
            
        vals = [root.val]
        if len(root.children) == 1:
            return vals
        for i, child in enumerate(root.children):
            root_height = max(c.height for j, c in enumerate(root.children) if j != i) + 1
            if max(child.height, root_height+1) == root.height:
                vals.append(child.val)
        return vals
            
    def constructTree(self, edges, val):
        root = self.TreeNode(val)
        neighbors, remains = list(), list()
        for edge in edges:
            if edge[0] == val or edge[1] == val:
                neighbors.append(edge if edge[0] == val else edge[::-1])
            else:
                remains.append(edge)
        
        if not neighbors:
            return root
        
        for edge in neighbors:
            heapq.heappush(root.children, self.constructTree(remains, edge[1]))
        root.height = root.children[0].height + 1
        return root
    
    def printTree(self, root):
        q = [root]
        while q:
            print([n.val for n in q])
            nextq = list()
            for node in q:
                nextq += node.children
            q = nextq