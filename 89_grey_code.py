class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        result = [0]
        add = 1
        for i in range(1, n + 1):
            l = len(result)
            # result.append(result[-1] + add)
            for j in range(l-1, -1, -1):
                result.append(result[j] + add)
            add *= 2
        return result

print(Solution().grayCode(3))