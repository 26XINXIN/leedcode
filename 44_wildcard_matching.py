class Edge:
    def __init__(self):
        self.u = 0
        self.v = 0

class OutGraph:
    def __init__(self):
        self.V = set()
        self.n = 0
        self.m = 0

        self.out_edges = dict()

    def insert(u, v):
        if u not in self.out_edges:
            self.out_edges[u] = [v]
        else:
            self.out_edges.append(v)


class Solution:
    def __init__(self):
        self.g = OutGraph()
        self.s = None
        self.p = None

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # DFS search
        self.s = s
        self.p = p
        if s == "" and p == "*":
            return True
        return self.NFA_DFS(0, 0)

    def NFA_DFS(self, idx, jdx):
        if idx == len(self.s) and jdx == len(self.p):
            return True
        elif idx != len(self.s) and jdx == len(self.p):
            return False
        elif idx == len(self.s) and jdx != len(self.p) and self.p[jdx:].count("*") == len(self.p) - jdx:
            return True
        elif idx == len(self.s) and jdx != len(self.p):
            return False

        if self.p[jdx] == "?":
            return self.NFA_DFS(idx + 1, jdx + 1)
        elif self.p[jdx] == "*":
            return self.NFA_DFS(idx + 1, jdx) or self.NFA_DFS(idx + 1, jdx + 1) or self.NFA_DFS(idx, jdx + 1)
        elif self.p[jdx] == self.s[idx]:
            return self.NFA_DFS(idx + 1, jdx + 1)
        else:
            return False
        
    def construct_nfa(p):
        for i in range(len(p)):
            """
            lp = i
            if p[i] == '(' or p[i] == '|':
                stack.append(i)
            elif p[i] == ')':
                _or = stack.pop()

                # 2-way or operator
                if p[_or] == '|':
                    lp = stack.pop()
                    self.g.insert(lp, _or+1)
                    self.g.insert(_or, i)
                elif p[_or] == '(':
                    lp = _or
                else:
                    print("err")
                    exit()

            # closure operator (uses 1-caractor lookahead)
            if i < len(p) - 1 and p[i+1] == "*":
                self.g.insert(lp, i+1)
                self.g.insert(i+1, lp)
            if p[i] == '(' or p[i] == "*" or p[i] == ")":
                self.g.insert(i, i+1)
            """

            if p[i] == "*":
                self.g.insert(i, i)
            self.g.insert(i, i+1)


        # stack size must be zero



