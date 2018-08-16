class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        min_sum = [triangle[0][0]]
        for l in range(1, len(triangle)):
            print(min_sum)
            next_min_sum = [0] * (l + 1)
            next_min_sum[0] = min_sum[0] + triangle[l][0]
            next_min_sum[-1] = min_sum[-1] + triangle[l][-1]
            for i in range(1, l):
                next_min_sum[i] = min(min_sum[i-1], min_sum[i]) + triangle[l][i]
            min_sum = next_min_sum
        return min(min_sum)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Solution().minimumTotal(triangle)