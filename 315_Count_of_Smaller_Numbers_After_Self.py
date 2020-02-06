class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.smaller = [0] * len(nums)
        self.mergeSort(enumerate(nums))
        return self.smaller

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left, right = self.mergeSort(nums[:mid]), self.mergeSort(nums[mid:]) 
        res = list()
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
                self.smaller[left[i][0]] += 1