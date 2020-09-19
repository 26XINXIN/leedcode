tid = 0

class TreeNode:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.pre = None
        self.id = tid
        tid += 1
    
    def contains(self, other):
        return self.width > other.width and self.height > other.height
    
    def contained_by(self, other):
        return self.width < other.width and self.height < other.height
    
    def contained_by(self, width, height):
        return self.width < width and self.height < height

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        leaves = dict()
        for env in envelopes:
            self.visited = set()
            max_len = 0
            max_pre = None
            for lid, leaf in leaves.items():
                pre = self.search(leaf, env)
                if pre is not None:
                    max_len = max(max_len, pre.length)
                    max_pre = pre
            node = TreeNode(max_len + 1, env[0], env[1])
            node.pre = max_pre
            if max_pre.id in leaves:
                leaves.pop(max_pre.id)
                leaves[node.id] = node
        
        return max(leaf.length for leaf in leaves)
                
    def search(self, leaf, env):
        width, height = env
        it = leaf
        while (
            it is not None
            and it.id not in self.visited
            and (it.width >= width or it.height >= height)
        ):
            self.visited.add(it.id)
            it = it.pre
        
        if it.id in self.visited or it is None:
            return None
        else:
            return it

    def covers(self, envelopes, i, j):
        return envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]