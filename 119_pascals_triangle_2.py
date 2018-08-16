class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        layer = [1]
        for n in range(2, rowIndex + 2):
            new_layer = [1] * n
            for i in range(1, n-1):
                new_layer[i] = layer[i-1] + layer[i]
            layer = new_layer
        return layer