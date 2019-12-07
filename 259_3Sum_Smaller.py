class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = 0
        nums.sort()
        for i in range(len(nums)-2):
            if 3 * nums[i] > target:
                break
            n += self.twoSumSmaller(nums[i+1:], target-nums[i])
        return n
    
    def twoSumSmaller(self, nums, target):
        n = 0
        for i in range(len(nums)-1):
            if 2 * nums[i] > target:
                break
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    n += 1
                else:
                    break
        return n