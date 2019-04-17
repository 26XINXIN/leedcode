from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums:
            return False
        
        from heapq import heappop, heappush
        num_set = list()
        for i in range(0, min(len(nums), k+1)):
            if self.binary_search(num_set, nums[i], t):
                return True
            heappush(num_set, nums[i])
            # print(num_set)
        for i in range(0, len(nums)-k-1):
            num_set = self.binary_remove(num_set, nums[i])
            # print(1, num_set)
            if self.binary_search(num_set, nums[i+k+1], t):
                return True
            heappush(num_set, nums[i+k+1])
            # print(2, num_set)
        return False
    
    def binary_search(self, nums, k, t):
        if not nums:
            return False
        mid = len(nums) // 2
        if nums[mid]-t <= k <= nums[mid]+t:
            return True
        elif k < nums[mid]-t:
            return self.binary_search(nums[:mid], k, t)
        else: 
            return self.binary_search(nums[mid+1:], k, t)
    
    def binary_remove(self, nums, k):
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            if k == nums[0]:
                return []
            else:
                return nums
        mid = len(nums) // 2
        # print(nums)
        if nums[mid] == k:
            # print('returns', )
            return nums[:mid] + nums[mid+1:]
        elif nums[mid] > k:
            return self.binary_remove(nums[:mid], k) + nums[mid:]
        else:
            return nums[:mid+1] + self.binary_remove(nums[mid+1:], k)