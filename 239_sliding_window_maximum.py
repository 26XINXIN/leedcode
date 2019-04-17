from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        if k == 1:
            return nums
        d = deque()
        result = list()
        for i, n in enumerate(nums):
            if d and d[0] < i-k+1: d.popleft()
            
            while d and nums[d[-1]] < n: d.pop()
            
            d.append(i)
            
            if i + 1 >= k: result.append(nums[d[0]])
        return result