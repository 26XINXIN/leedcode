class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.accu = [0]
        for i in range(len(self.nums)):
            self.accu.append(self.accu[-1] + self.nums[i])

    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        for j in range(i+1, len(self.nums)+1):
            self.accu[j] += diff

    def sumRange(self, i: int, j: int) -> int:
        return self.accu[j+1] - self.accu[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)