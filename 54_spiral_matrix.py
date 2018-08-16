class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        array = list()
        while len(matrix) > 0:
            array += matrix[0]
            matrix.pop(0)
            
            if len(matrix) == 0:
                break

            for i in range(len(matrix)-1):
                array.append(matrix[i][-1])
                matrix[i].pop()

            if len(matrix) == 0:
                break

            array += matrix[-1][::-1]
            matrix.pop()

            if len(matrix) == 0:
                break
            
            if len(matrix[0]) == 0:
                while len(matrix) > 0:
                    matrix.pop()
            
            if len(matrix) == 0:
                break

            for i in range(len(matrix) - 1, -1, -1):
                array.append(matrix[i][0])
                matrix[i].pop(0)
            
            if len(matrix[0]) == 0:
                while len(matrix) > 0:
                    matrix.pop()
        return array

                
