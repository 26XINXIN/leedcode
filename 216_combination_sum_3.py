from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.combinationSumMin(k, n, 1)
    
    def combinationSumMin(self, k, n, min_num): 
        # print(f"{k}, {n}, {min_num}, {max_num}")
        if n <= 0:
            return []
        if k == 1:
            if min_num <= n <= 9:
                return [[n]]
            else:
                return []
        result = list()
        for i in range(min_num, min(10, n+1)):
            sub_result = self.combinationSumMin(k-1, n-i, i+1)
            if sub_result:
                for sub in sub_result:
                    result.append([i] + sub)
        return result

k = 3
n = 9
print(Solution().combinationSum3(k, n))