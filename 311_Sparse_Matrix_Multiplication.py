class Solution:
    class crossNode:
        def __init__(self, val, i, j):
            self.i, self.j = i, j
            self.val = val
            self.right = None
            self.down = None
    
    class crossLink:
        def __init__(self, n, m):
            self.n, self.m = n, m
            self.row = [None] * n
            self.col = [None] * m
    
    
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a = self.constructCrossLink(A)
        b = self.constructCrossLink(B)
        
        C = [[0 for i in range(b.m)] for j in range(a.n)]
        for i in range(a.n):
            for j in range(b.m):
                row = a.row[i]
                col = b.col[j]
                val = 0
                while row and col:
                    if row.j == col.i:
                        val += row.val * col.val
                        row = row.right
                        col = col.down
                    elif row.j < col.i:
                        row = row.right
                    else:
                        col = col.down
                C[i][j] = val
        return C
    
    def constructCrossLink(self, M):
        n = len(M)
        m = len(M[0])
        c = self.crossLink(n, m)
        last_row = [None] * n
        last_col = [None] * m
        for i in range(n):
            for j in range(m):
                if M[i][j] != 0:
                    node = self.crossNode(M[i][j], i, j)
                    if c.row[i] is None:
                        c.row[i] = node
                        last_row[i] = node
                    else:
                        last_row[i].right = node
                        last_row[i] = node
                    if c.col[j] is None:
                        c.col[j] = node
                        last_col[j] = node
                    else:
                        last_col[j].down = node
                        last_col[j] = node
        return c
    
    def printCrossLink(self, M):
        for row in M.row:
            node = row
            while node:
                print((node.val, node.i, node.j), end=" ")
                node = node.right
            print('')
            
                