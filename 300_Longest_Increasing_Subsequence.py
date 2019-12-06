from heapq import heappush

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = [1]
        for i in range(1, len(nums)):
            max_len = 0
            for n, l in zip(nums[:i], length):
                if n < nums[i]:
                    max_len = max(max_len, l)
            length.append(max_len + 1)
        return max(length)

        
    # def heapsearch(self, heap, num):
        