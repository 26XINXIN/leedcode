class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append('x')
        for i in range(len(nums)):
            if i == nums[i]:
                continue
            pick = nums[i]
            while pick != 'x' and pick != i:
                tmp = nums[pick]
                nums[pick] = pick
                pick = tmp
                # pick, nums[pick] = nums[pick], pick
            nums[i] = pick
        return nums.index('x')