class Solution:
    def maxSubArrayLen(self, nums, k) -> int:
        S = [0]
        for n in nums:
            S.append(S[-1] + n)
        
        print(S)
        max_len = 0
        inverse_sum_index = dict()
        for i in range(1, len(S)):
            print(inverse_sum_index)
            if S[i] == k:
                max_len = max(max_len, i)
            else:
                if S[i] - k in inverse_sum_index:
                    max_len = max(max_len, (i - inverse_sum_index[S[i] - k]))
            if S[i] not in inverse_sum_index:
                inverse_sum_index[S[i]] = i
        return max_len


print(Solution().maxSubArrayLen([-2,-1,2,1], 1))