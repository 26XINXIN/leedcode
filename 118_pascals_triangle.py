class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        for n in range(2, numRows+1):
            layer = [1] * n
            for i in range(1, n-1):
                layer[i] = result[-1][i-1] + result[-1][i]
            result.append(layer)
        return result