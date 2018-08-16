class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        return self.C(1, n, k)
    
    def C(self, first, last, k):
        l = last - first + 1
        if l == k:
            return [[i for i in range(first, last + 1)]]
        elif k == 1:
            return [[i] for i in range(first, last + 1)]
        
        result = list()
        for i in range(first, first + l - k + 1):
            sub_C = self.C(i + 1, last, k-1)
            for c in sub_C:
                result.append([i] + c)
        return result
        
# print(Solution().combine(4, 2))
