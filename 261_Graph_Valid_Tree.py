class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            if n == 1:
                return True
            else:
                return False
        linked = set()
        for edge in edges:
            linked.add(edge[0])
            linked.add(edge[1])
        if len(linked) < n:
            return False
        path = list(edges[0])
        edges.pop(0)
        while edges:
            found = False
            for i in range(len(edges)):
                if edges[i][0] == path[-1] or edges[i][1] == path[-1]:
                    found = True
                    break
            if not found:
                path.pop()
                while path:
                    found = False
                    i = 0
                    while i < len(edges):
                        if edges[i][0] == path[-1] or edges[i][1] == path[-1]:
                            found = True
                            break
                        i += 1
                    if found:
                        break
                    path.pop()
                if not path:
                    return False
            edge = edges.pop(i)
            new_node = edge[0] if edge[1] == path[-1] else edge[1]
            if new_node in path:
                return False
            else:
                path.append(new_node)
        return True