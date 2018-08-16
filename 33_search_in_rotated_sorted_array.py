class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        base = 0
        if target == nums[0]:
            return 0
        elif target > nums[0]:
            base = 0
        else:
            base = -1
        return self.binary_search(nums, 0, len(nums), target, base)
    
    def binary_search(self, nums, left, right, target, base):
        print("{},{}".format(left, right))
        if left == right:
            if left < len(nums) and nums[left] == target:
                return left
            else:
                return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif base == 0 and nums[mid] < nums[0]:
            return self.binary_search(nums, left, mid, target, base)   
        elif base == -1 and nums[mid] > nums[-1]:
            return self.binary_search(nums, mid + 1, right, target, base)
        else:
            if nums[mid] < target:
                return self.binary_search(nums, mid + 1, right, target, base)
            else:
                return self.binary_search(nums, left, mid, target, base)

Solution().search([4, 5, 6, 7, 0, 1, 2], 0)