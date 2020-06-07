from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.visited = set()
        n_component = 0
        while len(edges) > 0:
            edges = self.search(edges)
            n_component += 1
        return n_component + n - len(self.visited)
    
    def search(self, edges):
        to_visit = deque()
        to_visit.append(edges[0][0])
        while len(to_visit) != 0:
            new_edges = list()
            node = to_visit.popleft()
            self.visited.add(node)
            for e in edges:
                if e[0] == node and e[1] not in self.visited:
                    to_visit.append(e[1])
                elif e[1] == node and e[0] not in self.visited:
                    to_visit.append(e[0])
                else:
                    new_edges.append(e)
            edges = new_edges
        return edges