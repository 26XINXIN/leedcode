class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return False
        base = 0
        out_of_range = 0
        if target == nums[0]:
            return True
        elif target > nums[0]:
            base = 0
            out_of_range = 1
            while out_of_range < len(nums) and nums[out_of_range] >= nums[out_of_range - 1]:
                out_of_range += 1
        else:
            base = -1
            out_of_range = len(nums) - 2
            while out_of_range >= 0 and nums[out_of_range] <= nums[out_of_range + 1]:
                out_of_range -= 1
        print(out_of_range)
        return self.binary_search(nums, 0, len(nums), target, base, out_of_range)
    
    def binary_search(self, nums, left, right, target, base, bound):
        print("{},{}".format(left, right))
        if left == right:
            if left < len(nums) and nums[left] == target:
                return True
            else:
                return False
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif base == 0 and mid >= bound:
            return self.binary_search(nums, left, mid, target, base, bound)   
        elif base == -1 and mid <= bound:
            return self.binary_search(nums, mid + 1, right, target, base, bound)
        else:
            if nums[mid] < target:
                return self.binary_search(nums, mid + 1, right, target, base, bound)
            else:
                return self.binary_search(nums, left, mid, target, base, bound)

Solution().search([1, 3, 1, 1], 3)