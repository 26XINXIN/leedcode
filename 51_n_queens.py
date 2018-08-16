class Solution:
    def __init__(self):
        self.n = None

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        # used for mark available position, 
        # 0 = available; 1 = unavailable
        if n == 0:
            return []
        elif n == 1:
            return [["Q"]]

        self.n = n
        solution = list()
        self.recursive_n_queens([], solution)
        result = list()
        for s in solution:
            r = list()
            for i in range(self.n):
                string = ""
                for j in range(self.n):
                    if s[i] == j:
                        string += "Q"
                    else:
                        string += "."
                r.append(string)
            result.append(r)
        return result

    def recursive_n_queens(self, prefix, solution):
        if len(prefix) == self.n:
            solution.append(prefix)
            return

        step = len(prefix)
        available = self.generate_possible_position(prefix)

        for i in range(self.n):
            if available[step][i] == 0:
                new_pre = list(prefix)
                new_pre.append(i)
                self.recursive_n_queens(new_pre, solution)


    def generate_possible_position(self, current):
        available = list()
        for i in range(self.n):
            available.append([0] * self.n)

        # row
        for i in range(len(current)):
            for j in range(self.n): 
                available[i][j] = 1

        #column
        for j in current:
            for i in range(self.n):
                available[i][j] = 1

        # grad
        for i in range(len(current)):
            for j in range(self.n):
                if 0 <= current[i] - j + i < self.n:
                    available[j][current[i] - j + i] = 1
                if 0 <= current[i] + j - i < self.n:
                    available[j][current[i] + j - i] = 1

        return available



    

